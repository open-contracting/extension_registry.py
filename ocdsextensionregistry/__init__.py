from ocdsextensionregistry.api import build_profile
from ocdsextensionregistry.codelist import Codelist
from ocdsextensionregistry.codelist_code import CodelistCode
from ocdsextensionregistry.extension import Extension
from ocdsextensionregistry.extension_registry import ExtensionRegistry
from ocdsextensionregistry.extension_version import ExtensionVersion
from ocdsextensionregistry.profile_builder import ProfileBuilder

EXTENSIONS_DATA = 'https://raw.githubusercontent.com/open-contracting/extension_registry/main/extensions.csv'
EXTENSION_VERSIONS_DATA = 'https://raw.githubusercontent.com/open-contracting/extension_registry/main/extension_versions.csv'

__all__ = (
    "EXTENSIONS_DATA",
    "EXTENSION_VERSIONS_DATA",
    "Codelist",
    "CodelistCode",
    "Extension",
    "ExtensionRegistry",
    "ExtensionVersion",
    "ProfileBuilder",
    "build_profile",
)
