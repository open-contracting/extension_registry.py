Profile Builder
===============

.. code:: python

    from ocdsextensionregistry import ProfileBuilder

    builder = ProfileBuilder('1__1__3', {
        'lots': 'v1.1.3',
        'bids': 'v1.1.3',
    })

This initializes a profile of OCDS 1.1.3 with two extensions. Alternately, you can pass a list of extensions' metadata URLs, base URLs and/or download URLs, for example:

.. code:: python

    builder = ProfileBuilder('1__1__3', [
      'https://raw.githubusercontent.com/open-contracting-extensions/ocds_coveredBy_extension/master/extension.json',
      'https://raw.githubusercontent.com/open-contracting-extensions/ocds_options_extension/master/',
      'https://github.com/open-contracting-extensions/ocds_techniques_extension/archive/master.zip',
    ])

After initializing the profile, you can then:

* :func:`release_schema_patch() <ocdsextensionregistry.profile_builder.ProfileBuilder.release_schema_patch>` to get the profile's patch of ``release-schema.json``
* :func:`patched_release_schema() <ocdsextensionregistry.profile_builder.ProfileBuilder.patched_release_schema>` to get ``release-schema.json``, after patching OCDS with the profile
* :func:`extension_codelists() <ocdsextensionregistry.profile_builder.ProfileBuilder.extension_codelists>` to get the profile's codelists
* :func:`patched_codelists() <ocdsextensionregistry.profile_builder.ProfileBuilder.patched_codelists>` to get the codelists, after patching OCDS with the profile
* :func:`extensions() <ocdsextensionregistry.profile_builder.ProfileBuilder.extensions>` to iterate over the profile's versions of extensions

API
---

.. autoclass:: ocdsextensionregistry.profile_builder.ProfileBuilder
    :special-members:
    :exclude-members: __weakref__
