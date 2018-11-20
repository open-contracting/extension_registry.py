import gettext
import json
import os
import sys
from collections import OrderedDict

from ocds_babel.translate import translate_codelist_data, translate_schema_data

from .base import BaseCommand
from ocdsextensionregistry import EXTENSIONS_DATA, EXTENSION_VERSIONS_DATA
from ocdsextensionregistry.exceptions import CommandError


def _translator(version, domain, localedir, language):
    domain = '{}/{}/{}'.format(version.id, version.version, domain)
    return gettext.translation(domain, localedir, languages=[language], fallback=language == 'en')


class Command(BaseCommand):
    name = 'generate-data-file'
    help = 'generates a data file in JSON format with all the information about versions of extensions'

    def add_arguments(self):
        self.add_argument('versions', nargs='*',
                          help="the versions of extensions to process (e.g. 'bids' or 'lots==master')")
        self.add_argument('-d', '--locale-dir',
                          help='a directory containing MO files'),
        self.add_argument('-l', '--languages',
                          help='a comma-separated list of translations to include (default all)'),
        self.add_argument('--extensions-url', help="the URL of the registry's extensions.csv",
                          default=EXTENSIONS_DATA)
        self.add_argument('--extension-versions-url', help="the URL of the registry's extension_versions.csv",
                          default=EXTENSION_VERSIONS_DATA)

    def handle(self):
        if self.args.languages and not self.args.locale_dir:
            self.subparser.error('--locale-dir is required if --languages is set.')

        data = OrderedDict()
        languages = {'en'}
        localedir = self.args.locale_dir

        if localedir:
            available_translations = [n for n in os.listdir(localedir) if os.path.isdir(os.path.join(localedir, n))]
            if self.args.languages:
                for language in self.args.languages.split(','):
                    if language in available_translations:
                        languages.add(language)
                    else:
                        self.subparser.error('translations to {} are not available'.format(language))
            else:
                languages.update(available_translations)

        for version in self.versions():
            # Add the extension's data.
            if version.id not in data:
                data[version.id] = OrderedDict([
                    ('id', version.id),
                    ('category', version.category),
                    ('core', version.core),
                    ('name', OrderedDict()),
                    ('description', OrderedDict()),
                    ('latest_version', None),
                    ('versions', OrderedDict()),
                ])

            # Add the version's metadata.
            version_data = OrderedDict([
                ('id', version.id),
                ('date', version.date),
                ('version', version.version),
                ('base_url', version.base_url),
                ('download_url', version.download_url),
                ('metadata', version.metadata),
                ('schemas', OrderedDict()),
                ('codelists', OrderedDict()),
                ('docs', OrderedDict()),
                ('readme', OrderedDict({
                    'en': version.remote('README.md'),
                })),
            ])

            for language in languages:
                # Add the version's schema.
                translator = _translator(version, 'schema', localedir, language)
                for name in ('record-package-schema.json', 'release-package-schema.json', 'release-schema.json'):
                    if name not in version_data['schemas']:
                        version_data['schemas'][name] = OrderedDict()

                    if name in version.schemas:
                        schema = version.schemas[name]
                        translation = translate_schema_data(schema, translator)
                        version_data['schemas'][name][language] = translation

                # Add the version's codelists.
                translator = _translator(version, 'codelists', localedir, language)
                for name in sorted(version.codelists):
                    if name not in version_data['codelists']:
                        version_data['codelists'][name] = OrderedDict([
                            ('fieldnames', OrderedDict()),
                            ('rows', OrderedDict()),
                        ])

                    codelist = version.codelists[name]

                    for fieldname in codelist.fieldnames:
                        if fieldname not in version_data['codelists'][name]['fieldnames']:
                            version_data['codelists'][name]['fieldnames'][fieldname] = OrderedDict()
                        translation = translator.gettext(fieldname)
                        version_data['codelists'][name]['fieldnames'][fieldname][language] = translation

                    translations = translate_codelist_data(codelist, translator)
                    for translation in translations:
                        code = translation[version_data['codelists'][name]['fieldnames']['Code'][language]]
                        if code not in version_data['codelists'][name]['rows']:
                            version_data['codelists'][name]['rows'][code] = OrderedDict()
                        version_data['codelists'][name]['rows'][code][language] = translation

            # Add the version's documentation.
            for name in sorted(version.docs):
                version_data['docs'][name] = OrderedDict({
                    'en': version.docs[name],
                })

            data[version.id]['versions'][version.version] = version_data

        for _id in data:
            # Determine the latest version.
            versions = data[_id]['versions']
            if len(versions) == 1:
                latest_version = list(versions)[0]
            elif 'master' in versions:
                latest_version = 'master'
            else:
                dated = list(filter(lambda item: item[1]['date'], versions.items()))
                if dated:
                    latest_version = sorted(dated, key=lambda item: item[1]['date'])[-1][0]
                else:
                    raise CommandError("Couldn't determine latest version of {}".format(_id))

            # Apply the latest version.
            data[_id]['latest_version'] = latest_version
            for field in ('name', 'description'):
                data[_id][field] = data[_id]['versions'][latest_version]['metadata'][field]

        json.dump(data, sys.stdout, ensure_ascii=False, indent=2, separators=(',', ': '))
