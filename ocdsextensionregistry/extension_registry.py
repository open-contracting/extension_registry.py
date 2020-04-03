"""
Filter the versions of extensions in the registry, and access information about matching versions:

.. code:: python

    from ocdsextensionregistry import ExtensionRegistry

    extensions_url = 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/extensions.csv'
    extension_versions_url = 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/extension_versions.csv'

    registry = ExtensionRegistry(extension_versions_url, extensions_url)
    for version in registry.filter(core=True, version='v1.1.3', category='tender'):
        print('The {0.metadata[name][en]} extension ("{0.id}") is maintained at {0.repository_html_page}'.format(version))
        print('Run `git clone {0.repository_url}` to make a local copy in a {0.repository_name} directory'.format(version))
        print('Get its patch at {0.base_url}release-schema.json\\n'.format(version))

Output::

    The Enquiries extension ("enquiries") is maintained at https://github.com/open-contracting-extensions/ocds_enquiry_extension
    Run `git clone git@github.com:open-contracting-extensions/ocds_enquiry_extension.git` to make a local copy in a ocds_enquiry_extension directory
    Get its patch at https://raw.githubusercontent.com/open-contracting-extensions/ocds_enquiry_extension/v1.1.3/release-schema.json

To work with the files within a version of an extension:

* :func:`metadata <ocdsextensionregistry.extension_version.ExtensionVersion.metadata>` parses and provides consistent access to the information in ``extension.json``
* :func:`schemas <ocdsextensionregistry.extension_version.ExtensionVersion.schemas>` returns the parsed contents of schema files
* :func:`codelists <ocdsextensionregistry.extension_version.ExtensionVersion.codelists>` returns the parsed contents of codelist files (see more below)
* :func:`files <ocdsextensionregistry.extension_version.ExtensionVersion.files>` returns the unparsed contents of all files

See additional details in :doc:`extension_version`.
"""  # noqa

import csv
from io import StringIO
from urllib.parse import urlparse

import requests
import requests_cache

from .exceptions import DoesNotExist, MissingExtensionMetadata
from .extension import Extension
from .extension_version import ExtensionVersion

requests_cache.install_cache(backend='memory')


class ExtensionRegistry:
    def __init__(self, extension_versions_data, extensions_data=None):
        """
        Accepts extension_versions.csv and, optionally, extensions.csv as either URLs or data (as string) and reads
        them into ExtensionVersion objects. If extensions_data is not provided, the extension versions will not have
        category or core properties.
        """
        self.versions = []

        # If extensions data is provided, prepare to merge it with extension versions data.
        extensions = {}
        if extensions_data:
            extensions_data = self._resolve(extensions_data)
            for row in csv.DictReader(StringIO(extensions_data)):
                extension = Extension(row)
                extensions[extension.id] = extension

        extension_versions_data = self._resolve(extension_versions_data)
        for row in csv.DictReader(StringIO(extension_versions_data)):
            version = ExtensionVersion(row)
            if version.id in extensions:
                version.update(extensions[version.id])
            self.versions.append(version)

    def filter(self, **kwargs):
        """
        Returns the extension versions in the registry that match the keyword arguments.

        :raises MissingExtensionMetadata: if the keyword arguments refer to extensions data, but the extension registry
                                          was not initialized with extensions data
        """
        try:
            return list(filter(lambda ver: all(getattr(ver, k) == v for k, v in kwargs.items()), self.versions))
        except AttributeError as e:
            self._handle_attribute_error(e)

    def get(self, **kwargs):
        """
        Returns the first extension version in the registry that matches the keyword arguments.

        :raises DoesNotExist: if no extension version matches the keyword arguments
        :raises MissingExtensionMetadata: if the keyword arguments refer to extensions data, but the extension registry
                                          was not initialized with extensions data
        """
        try:
            return next(ver for ver in self.versions if all(getattr(ver, k) == v for k, v in kwargs.items()))
        except StopIteration:
            raise DoesNotExist('Extension version matching {!r} does not exist.'.format(kwargs))
        except AttributeError as e:
            self._handle_attribute_error(e)

    def __iter__(self):
        """
        Iterates over the extension versions in the registry.
        """
        for version in self.versions:
            yield version

    def _resolve(self, data_or_url):
        parsed = urlparse(data_or_url)
        if parsed.scheme:
            if parsed.scheme == 'file':
                with open(data_or_url[7:]) as f:
                    return f.read()
            return requests.get(data_or_url).text
        return data_or_url

    def _handle_attribute_error(self, e):
        if "'category'" in str(e.args) or "'core'" in str(e.args):
            raise MissingExtensionMetadata('ExtensionRegistry must be initialized with extensions data.') from e
        raise
