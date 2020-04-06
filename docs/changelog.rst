Changelog
=========

0.0.18 (2020-04-06)
~~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.__repr__` falls back to Base URL and Download URL if Id or Version is blank.
-  The ``generate-data-files`` command uses a null translator if an MO file is missing.

0.0.17 (2020-04-03)
~~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.remote` raises :exception:`~ocdsextensionregistry.exceptions.DoesNotExist` instead of :exception:`KeyError` if a file does not exist.
-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: Add :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.__repr__`.
-  :class:`~ocdsextensionregistry.extension.Extension`: Add :meth:`~ocdsextensionregistry.extension.Extension.__repr__`.

0.0.16 (2019-11-20)
~~~~~~~~~~~~~~~~~~~

-  Add support for Sphinx>=1.6.

0.0.15 (2019-09-30)
~~~~~~~~~~~~~~~~~~~

-  Add a ``update_codelist_urls`` parameter to :meth:`ocdsextensionregistry.api.build_profile` to modify codelist reference URLs.

0.0.14 (2019-09-18)
~~~~~~~~~~~~~~~~~~~

-  Use in-memory HTTP requests cache.

0.0.13 (2019-08-29)
~~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.profile_builder.ProfileBuilder`: Add a ``schema`` parameter to :meth:`~ocdsextensionregistry.profile_builder.ProfileBuilder.patched_release_schema` and :meth:`~ocdsextensionregistry.profile_builder.ProfileBuilder.release_package_schema` methods to override the release schema or release package schema.

0.0.12 (2019-08-29)
~~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.profile_builder.ProfileBuilder`: Unregistered extensions are now supported by the profile builder. The ``extension_versions`` argument to :meth:`~ocdsextensionregistry.profile_builder.ProfileBuilder.__init__` can be a list of extensions' metadata URLs, base URLs and/or download URLs.
-  :class:`~ocdsextensionregistry.profile_builder.ProfileBuilder`: Add an ``extension_field`` parameter to :meth:`~ocdsextensionregistry.profile_builder.ProfileBuilder.release_schema_patch` and :meth:`~ocdsextensionregistry.profile_builder.ProfileBuilder.patched_release_schema` methods to annotate all definitions and properties with extension names.
-  Add :meth:`ocdsextensionregistry.utils.get_latest_version`, to return the identifier of the latest version from a list of versions of the same extension.

0.0.11 (2019-06-26)
~~~~~~~~~~~~~~~~~~~

The ``generate-pot-files`` and ``generate-data-files`` commands can now be run offline (see `documentation <https://ocdsextensionregistry.readthedocs.io/en/latest/cli.html>`__ for details).

-  :class:`~ocdsextensionregistry.extension_registry.ExtensionRegistry`: Support the ``file://`` scheme for the ``extension_versions_data`` and ``extensions_data`` arguments to :meth:`~ocdsextensionregistry.extension_registry.ExtensionRegistry.__init__`. This means the ``--extension-versions-url`` and ``--extensions-url`` CLI options can now refer to local files.
-  Add a ``--versions-dir`` option to the ``generate-pot-files`` and ``generate-data-files`` commands to specify a local directory of extension versions.
-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: Add :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.available_in_bulk`, to return whether the extension’s files are available in bulk.
-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: Add :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.zipfile`, to return a ZIP archive of the extension’s files.
-  Upgrade to ocds-babel 0.1.0.

0.0.10 (2019-01-28)
~~~~~~~~~~~~~~~~~~~

-  Fix invalid ``dependencies`` in ``extension.json``.

0.0.9 (2019-01-23)
~~~~~~~~~~~~~~~~~~

-  Drop support for ``docs/`` directory in extensions.
-  Use UTF-8 characters in JSON files when building profiles.
-  No longer write extension readme files when building profiles.

0.0.8 (2019-01-18)
~~~~~~~~~~~~~~~~~~

-  Fix rate limiting error when getting publisher names from GitHub in ``generate-data-file`` tool.

0.0.7 (2019-01-18)
~~~~~~~~~~~~~~~~~~

-  Add ``publisher`` data to the ``generate-data-file`` tool.
-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: Add :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.repository_user` and :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.repository_user_page` properties, to return user or organization to which the extension’s repository belongs.

0.0.6 (2018-11-20)
~~~~~~~~~~~~~~~~~~

-  Add command-line tools (see `documentation <https://ocdsextensionregistry.readthedocs.io/en/latest/cli.html>`__ for details).
-  Fix edge case so that ``metadata`` language maps are ordered, even if ``extension.json`` didn’t have language maps.

0.0.5 (2018-10-31)
~~~~~~~~~~~~~~~~~~

-  Add  :class:`~ocdsextensionregistry.profile_builder.ProfileBuilder`, :class:`~ocdsextensionregistry.codelist.Codelist`, :class:`~ocdsextensionregistry.codelist_code.CodelistCode` classes.
-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`:

   -  Add :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.files` property, to return the contents of all files within the extension.
   -  Add :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.schemas` property, to return the schemas.
   -  Add :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.codelists` property, to return the codelists.
   -  Add :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.docs` property, to return the contents of documentation files within the extension.
   -  The :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.metadata` property normalizes the contents of ``extension.json`` to provide consistent access.

0.0.4 (2018-06-27)
~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: The :attr:`~ocdsextensionregistry.extension_version.ExtensionVersion.metadata` property is cached.

0.0.3 (2018-06-27)
~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: Add :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.remote` method, to return the contents of a file within the extension.
-  :class:`~ocdsextensionregistry.extension_version.ExtensionVersion`: Add :meth:`~ocdsextensionregistry.extension_version.ExtensionVersion.as_dict` method, to avoid returning private properties.
-  :class:`~ocdsextensionregistry.extension_version.Extension`: Add :meth:`~ocdsextensionregistry.extension.Extension.as_dict` method, to avoid returning private properties.

0.0.2 (2018-06-12)
~~~~~~~~~~~~~~~~~~

-  :class:`~ocdsextensionregistry.extension_registry.ExtensionRegistry`:

   -  Add :meth:`~ocdsextensionregistry.extension_registry.ExtensionRegistry.get` method, to get a specific extension version.
   -  Make it iterable, to iterate over all extension versions.
   -  Remove ``all()`` method.

-  Add package-specific exceptions.

0.0.1 (2018-06-11)
~~~~~~~~~~~~~~~~~~

First release.
