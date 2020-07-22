import json
import os
from io import BytesIO
from urllib.parse import urlparse
from zipfile import ZipFile

import requests
import requests_cache

from .exceptions import UnknownLatestVersion

if os.name == 'nt':
    encoding = 'cp1252'
else:
    encoding = 'utf-8'

requests_cache.install_cache(backend='memory')


def json_dump(data, io):
    """
    Dumps JSON to a file-like object.
    """
    json.dump(data, io, ensure_ascii=False, indent=2, separators=(',', ': '))


def get_latest_version(versions):
    """
    Returns the identifier of the latest version from a list of versions of the same extension.

    :raises UnknownLatestVersion: if the latest version of the extension can't be determined
    """
    if len(versions) == 1:
        return versions[0]

    for version in versions:
        if version.version == 'master':
            return version

    dated = list(filter(lambda version: version.date, versions))
    if dated:
        return max(dated, key=lambda version: version.date)

    raise UnknownLatestVersion


def _resolve(data_or_url):
    parsed = urlparse(data_or_url)

    if parsed.scheme:
        if parsed.scheme == 'file':
            with open(data_or_url[7:]) as f:
                return f.read()

        response = requests.get(data_or_url)
        response.raise_for_status()
        return response.text

    return data_or_url


def _resolve_zip(url, root=''):
    parsed = urlparse(url)

    if parsed.scheme == 'file':
        io = BytesIO()
        with ZipFile(io, 'w') as zipfile:
            zipfile.write(url[7:])
            for root, dirs, files in os.walk(os.path.join(url[7:], root)):
                for directory in dirs:
                    if directory == '__pycache__':
                        dirs.remove(directory)
                for file in sorted(files):
                    zipfile.write(os.path.join(root, file))
    else:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
        io = BytesIO(response.content)

    return ZipFile(io)
