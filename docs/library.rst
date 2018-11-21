Programmatic Access
===================

Examples
--------

Extension Registry
~~~~~~~~~~~~~~~~~~

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

    The Enquiries extension ("enquiries") is maintained at https://github.com/open-contracting/ocds_enquiry_extension
    Run `git clone git@github.com:open-contracting/ocds_enquiry_extension.git` to make a local copy in a ocds_enquiry_extension directory
    Get its patch at https://raw.githubusercontent.com/open-contracting/ocds_enquiry_extension/v1.1.3/release-schema.json

To work with the files within a version of an extension:

* :func:`metadata <ocdsextensionregistry.extension_version.ExtensionVersion.metadata>` parses and provides consistent access to the information in ``extension.json``
* :func:`schemas <ocdsextensionregistry.extension_version.ExtensionVersion.schemas>` returns the parsed contents of schema files
* :func:`codelists <ocdsextensionregistry.extension_version.ExtensionVersion.codelists>` returns the parsed contents of codelist files (see more below)
* :func:`docs <ocdsextensionregistry.extension_version.ExtensionVersion.docs>` returns the unparsed contents of documentation files
* :func:`files <ocdsextensionregistry.extension_version.ExtensionVersion.files>` returns the unparsed contents of all files

See all details in :doc:`api/extension_version`.

Codelists
~~~~~~~~~

.. code:: python

    from ocdsextensionregistry import Codelist

Create a new codelist:

.. code:: python

    codelist = Codelist('+partyRole.csv')

Add codes to the codelist (you can provide any iterable, including a :code:`csv.DictReader`):

.. code:: python

    codelist.extend([
        {'Code': 'publicAuthority', 'Title': 'Public authority', 'Description': ''},
        {'Code': 'bidder', 'Title': 'Bidder', 'Description': ''}
    ])

Iterate over the codes in the codelist:

.. code:: python

    [code['Title'] for code in codelist]  # ['Public authority', 'Bidder']

Read the codelists' codes and fieldnames:

.. code:: python

    codelist.codes  # ['publicAuthority', 'bidder']
    codelist.fieldnames  # ['Code', 'Title', 'Description']

Determine whether the codelist adds or removes codes from another codelist:

.. code:: python

    codelist.patch  # True
    codelist.addend  # True
    codelist.subtrahend  # False

Get the name of the codelist it modifies:

.. code:: python

    codelist.basename  # 'partyRole.csv'

See all details in :doc:`api/codelist`.

Profile Builder
~~~~~~~~~~~~~~~

.. code:: python

    from ocdsextensionregistry import ProfileBuilder

    builder = ProfileBuilder('1__1__3', {
        'lots': 'v1.1.3',
        'bids': 'v1.1.3',
    })

This initializes a profile of OCDS 1.1.3 with two extensions. You can then:

* :func:`release_schema_patch() <ocdsextensionregistry.profile_builder.ProfileBuilder.release_schema_patch>` to get the profile's patch of ``release-schema.json``
* :func:`patched_release_schema() <ocdsextensionregistry.profile_builder.ProfileBuilder.patched_release_schema>` to get ``release-schema.json``, after patching OCDS with the profile
* :func:`extension_codelists() <ocdsextensionregistry.profile_builder.ProfileBuilder.extension_codelists>` to get the profile's codelists
* :func:`patched_codelists() <ocdsextensionregistry.profile_builder.ProfileBuilder.patched_codelists>` to get the codelists, after patching OCDS with the profile
* :func:`extensions() <ocdsextensionregistry.profile_builder.ProfileBuilder.extensions>` to iterate over the profile's versions of extensions

See all details in :doc:`api/profile_builder`.

API documentation
~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   api/extension_registry
   api/extension_version
   api/extension
   api/codelist
   api/codelist_code
   api/profile_builder
   api/api
   api/exceptions
