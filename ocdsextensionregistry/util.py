import json

from .exceptions import UnknownLatestVersion


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
