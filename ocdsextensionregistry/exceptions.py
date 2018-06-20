class OCDSExtensionRegistryError(Exception):
    """Base class for exceptions from within this package"""


class DoesNotExist(OCDSExtensionRegistryError):
    """Raised if an object wasn't found for the given parameters"""


class MissingExtensionMetadata(OCDSExtensionRegistryError):
    """Raised if a method call requires extensions metadata, with which the extension registry was not initialized"""
