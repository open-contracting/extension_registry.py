class OCDSExtensionRegistryError(Exception):
    """Base class for exceptions from within this package"""


class DoesNotExist(OCDSExtensionRegistryError):
    """Raised if an object wasn't found for the given parameters"""


class MissingExtensionMetadata(OCDSExtensionRegistryError):
    """Raised if a method call requires extensions metadata, with which the extension registry was not initialized"""


class NotAvailableInBulk(OCDSExtensionRegistryError):
    """Raised if files are required to be available in bulk, but are not"""


class UnknownLatestVersion(OCDSExtensionRegistryError):
    """Raised if the latest version of an extension can't be determined"""


class CommandError(OCDSExtensionRegistryError):
    """Errors from within this package's CLI"""


class OCDSExtensionRegistryWarning(UserWarning):
    """Base class for warnings from within this package"""


# The attributes are used by lib-cove-ocds.
class ExtensionWarning(OCDSExtensionRegistryWarning):
    """Used when an extension file can't be read."""

    def __init__(self, extension, exc):
        self.extension = extension
        self.exc = exc

    def __str__(self):
        cls = type(self.exc)
        return f"{self.extension}: {cls.__module__}.{cls.__name__}: {self.exc}"


# The attributes are used by lib-cove-ocds.
class ExtensionCodelistWarning(OCDSExtensionRegistryWarning):
    """Used when a codelist file can't be read."""

    def __init__(self, extension, codelist, exc):
        self.extension = extension
        self.codelist = codelist
        self.exc = exc

    def __str__(self):
        cls = type(self.exc)
        return f"{self.extension}({self.codelist}): {cls.__module__}.{cls.__name__}: {self.exc}"
