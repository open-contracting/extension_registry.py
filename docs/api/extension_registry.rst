Extension Registry
==================

Filter the versions of extensions in the registry, and access information about matching versions:

.. code:: python

    from ocdsextensionregistry import ExtensionRegistry

    extensions_url = 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/extensions.csv'
    extension_versions_url = 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/extension_versions.csv'

    registry = ExtensionRegistry(extension_versions_url, extensions_url)
    for version in registry.filter(core=True, version='v1.1.3', category='tender'):
        print('The {0.metadata[name][en]} extension ("{0.id}") is maintained at {0.repository_html_page}'.format(version))
        print('Run `git clone {0.repository_url}` to make a local copy in a {0.repository_name} directory'.format(version))
        print('Get its patch at {0.base_url}release-schema.json\n'.format(version))

Output::

    The Enquiries extension ("enquiries") is maintained at https://github.com/open-contracting-extensions/ocds_enquiry_extension
    Run `git clone git@github.com:open-contracting-extensions/ocds_enquiry_extension.git` to make a local copy in a ocds_enquiry_extension directory
    Get its patch at https://raw.githubusercontent.com/open-contracting-extensions/ocds_enquiry_extension/v1.1.3/release-schema.json

To work with the files within a version of an extension:

* :func:`metadata <ocdsextensionregistry.extension_version.ExtensionVersion.metadata>` parses and provides consistent access to the information in ``extension.json``
* :func:`schemas <ocdsextensionregistry.extension_version.ExtensionVersion.schemas>` returns the parsed contents of schema files
* :func:`codelists <ocdsextensionregistry.extension_version.ExtensionVersion.codelists>` returns the parsed contents of codelist files (see more below)
* :func:`files <ocdsextensionregistry.extension_version.ExtensionVersion.files>` returns the unparsed contents of all files

See additional details in :doc:`api/extension_version`.

API
---

.. autoclass:: ocdsextensionregistry.extension_registry.ExtensionRegistry
    :special-members:
    :exclude-members: __weakref__
