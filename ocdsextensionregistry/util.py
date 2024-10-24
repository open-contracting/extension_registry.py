import json
import os
import warnings
from io import BytesIO
from urllib.parse import urlsplit
from zipfile import ZipFile

from requests.adapters import HTTPAdapter
from requests_cache import NEVER_EXPIRE, CachedSession

from ocdsextensionregistry.exceptions import UnknownLatestVersion

# For example: "file:///C|/tmp" or "file:///tmp"
FILE_URI_OFFSET = 8 if os.name == 'nt' else 7

DEFAULT_MINOR_VERSION = '1.1'

# https://requests-cache.readthedocs.io/en/stable/user_guide/troubleshooting.html#common-error-messages
# https://docs.python.org/3/library/socket.html#constants
warnings.filterwarnings(
    'ignore',
    category=ResourceWarning,
    message=r"^unclosed <ssl\.SSLSocket fd=\d+, family=AddressFamily\.AF_INET6?, type=SocketKind\.SOCK_STREAM, ",
)

# https://2.python-requests.org/projects/3/api/#requests.adapters.HTTPAdapter
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#customizing-pool-behavior
adapter = HTTPAdapter(max_retries=3, pool_maxsize=int(os.getenv('REQUESTS_POOL_MAXSIZE', '10')))
session = CachedSession(backend='memory', expire_after=os.getenv('REQUESTS_CACHE_EXPIRE_AFTER', NEVER_EXPIRE))
session.mount('https://', adapter)
session.mount('http://', adapter)


def json_dump(data, io):
    """Dump JSON to a file-like object."""
    json.dump(data, io, ensure_ascii=False, indent=2)


def get_latest_version(versions):
    """
    Return the identifier of the latest version from a list of versions of the same extension.

    :raises UnknownLatestVersion: if the latest version of the extension can't be determined
    """
    if len(versions) == 1:
        return versions[0]

    version_numbers = {version.version: version for version in versions}
    if 'master' in version_numbers:
        return version_numbers['master']
    if DEFAULT_MINOR_VERSION in version_numbers:
        return version_numbers[DEFAULT_MINOR_VERSION]

    dated = [version for version in versions if version.date]
    if dated:
        return max(dated, key=lambda version: version.date)

    raise UnknownLatestVersion


def _resolve(data_or_url):
    parsed = urlsplit(data_or_url)

    if parsed.scheme:
        if parsed.scheme == 'file':
            with open(data_or_url[FILE_URI_OFFSET:]) as f:
                return f.read()

        response = session.get(data_or_url)
        response.raise_for_status()
        return response.text

    return data_or_url


def _resolve_zip(url, base=''):
    parsed = urlsplit(url)

    if parsed.scheme == 'file':
        if url.endswith('.zip'):
            with open(url[FILE_URI_OFFSET:], 'rb') as f:
                io = BytesIO(f.read())
        else:
            io = BytesIO()
            with ZipFile(io, 'w') as zipfile:
                zipfile.write(url[FILE_URI_OFFSET:], arcname='zip/')
                for root, dirs, files in os.walk(os.path.join(url[FILE_URI_OFFSET:], base)):
                    for directory in dirs:
                        if directory == '__pycache__':
                            dirs.remove(directory)
                    for file in sorted(files):
                        zipfile.write(os.path.join(root, file), arcname=f'zip/{file}')
    else:
        response = session.get(url, allow_redirects=True)
        response.raise_for_status()
        io = BytesIO(response.content)

    return ZipFile(io)
