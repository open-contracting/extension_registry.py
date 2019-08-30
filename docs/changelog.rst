Changelog
=========

0.0.12 (2019-XX-XX)
~~~~~~~~~~~~~~~~~~~

- Unregistered extensions are now supported by the profile builder. The ``extension_versions`` argument to ``ProfileBuilder`` can be a list of extensions' metadata URLs, base URLs and/or download URLs.
- Add an ``add_extension_field`` parameter to ``ProfileBuilder``'s ``release_schema_patch`` and ``patched_release_schema`` methods to annotate all definitions and properties with extension names.
- Add a ``get_latest_version`` function to ``ocdsextensionregistry.utils``, to return the identifier of the latest version from a list of versions of the same extension.

0.0.11 (2019-06-26)
~~~~~~~~~~~~~~~~~~~

The ``generate-pot-files`` and ``generate-data-files`` commands can now be run offline (see `documentation <https://ocdsextensionregistry.readthedocs.io/en/latest/cli.html>`__ for details).

-  Support the ``file`` scheme for the ``extension_versions_data`` and ``extensions_data`` arguments to ``ExtensionRegistry``. This means the ``--extension-versions-url`` and ``--extensions-url`` CLI options can now refer to local files.
-  Add a ``--versions-dir`` option to the ``generate-pot-files`` and ``generate-data-files`` commands to specify a local directory of extension versions.
-  Add ``available_in_bulk()`` method to ``ExtensionVersion``, to return whether the extension’s files are available in bulk.
-  Add ``zipfile()`` method to ``ExtensionVersion``, to return a ZIP archive of the extension’s files.
-  Upgrade to ocds-babel 0.1.0.

.. _section-1:

0.0.10 (2019-01-28)
~~~~~~~~~~~~~~~~~~~

-  Fix invalid ``dependencies`` in ``extension.json``.

.. _section-2:

0.0.9 (2019-01-23)
~~~~~~~~~~~~~~~~~~

-  Drop support for ``docs/`` directory in extensions.
-  Use UTF-8 characters in JSON files when building profiles.
-  No longer write extension readme files when building profiles.

.. _section-3:

0.0.8 (2019-01-18)
~~~~~~~~~~~~~~~~~~

-  Fix rate limiting error when getting publisher names from GitHub in ``generate-data-file`` tool.

.. _section-4:

0.0.7 (2019-01-18)
~~~~~~~~~~~~~~~~~~

-  Add ``publisher`` data to the ``generate-data-file`` tool.
-  Add ``repository_user`` and ``repository_user_page`` properties to ``ExtensionVersion``, to return user or organization to which the extension’s repository belongs.

.. _section-5:

0.0.6 (2018-11-20)
~~~~~~~~~~~~~~~~~~

-  Add command-line tools (see `documentation <https://ocdsextensionregistry.readthedocs.io/en/latest/cli.html>`__ for details).
-  Fix edge case so that ``metadata`` language maps are ordered, even if ``extension.json`` didn’t have language maps.

.. _section-6:

0.0.5 (2018-10-31)
~~~~~~~~~~~~~~~~~~

-  Add ``ProfileBuilder``, ``Codelist``, ``CodelistCode`` classes.
-  Add ``files`` property to ``ExtensionVersion``, to return the contents of all files within the extension.
-  Add ``schemas`` property to ``ExtensionVersion``, to return the schemas.
-  Add ``codelists`` property to ``ExtensionVersion``, to return the codelists.
-  Add ``docs`` property to ``ExtensionVersion``, to return the contents of documentation files within the extension.
-  The ``metadata`` property of ``ExtensionVersion`` normalizes the contents of ``extension.json`` to provide consistent access.

.. _section-7:

0.0.4 (2018-06-27)
~~~~~~~~~~~~~~~~~~

-  The ``metadata`` property of ``ExtensionVersion`` is cached.

.. _section-8:

0.0.3 (2018-06-27)
~~~~~~~~~~~~~~~~~~

-  Add ``remote(basename)`` method to ``ExtensionVersion``, to return the contents of a file within the extension.
-  Add ``as_dict()`` method to ``Extension`` and ``ExtensionVersion``, to avoid returning private properties.

.. _section-9:

0.0.2 (2018-06-12)
~~~~~~~~~~~~~~~~~~

-  Add ``get(**kwargs)`` method to ``ExtensionRegistry``, to get a specific extension version.
-  Make ``ExtensionRegistry`` iterable, to iterate over all extension versions.
-  Remove ``all()`` method from ``ExtensionRegistry``.
-  Add package-specific exceptions.

.. _section-10:

0.0.1 (2018-06-11)
~~~~~~~~~~~~~~~~~~

First release.
