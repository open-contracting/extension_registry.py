# Changelog

## 0.0.9 (2019-01-23)

* Drop support for `docs/` directory in extensions.
* Use UTF-8 characters in JSON files when building profiles.
* No longer write extension readme files when building profiles.

## 0.0.8 (2019-01-18)

* Fix rate limiting error when getting publisher names from GitHub in `generate-data-file` tool.

## 0.0.7 (2019-01-18)

* Add `publisher` data to the `generate-data-file` tool.
* Add `repository_user` and `repository_user_page` properties to `ExtensionVersion`, to return user or organization to which the extension's repository belongs.

## 0.0.6 (2018-11-20)

* Add command-line tools (see [documentation](https://ocdsextensionregistry.readthedocs.io/en/latest/cli.html) for details).
* Fix edge case so that `metadata` language maps are ordered, even if `extension.json` didn't have language maps.

## 0.0.5 (2018-10-31)

* Add `ProfileBuilder`, `Codelist`, `CodelistCode` classes.
* Add `files` property to `ExtensionVersion`, to return the contents of all files within the extension.
* Add `schemas` property to `ExtensionVersion`, to return the schemas.
* Add `codelists` property to `ExtensionVersion`, to return the codelists.
* Add `docs` property to `ExtensionVersion`, to return the contents of documentation files within the extension.
* The `metadata` property of `ExtensionVersion` normalizes the contents of `extension.json` to provide consistent access.

## 0.0.4 (2018-06-27)

* The `metadata` property of `ExtensionVersion` is cached.

## 0.0.3 (2018-06-27)

* Add `remote(basename)` method to `ExtensionVersion`, to return the contents of a file within the extension.
* Add `as_dict()` method to `Extension` and `ExtensionVersion`, to avoid returning private properties.

## 0.0.2 (2018-06-12)

* Add `get(**kwargs)` method to `ExtensionRegistry`, to get a specific extension version.
* Make `ExtensionRegistry` iterable, to iterate over all extension versions.
* Remove `all()` method from `ExtensionRegistry`.
* Add package-specific exceptions.

## 0.0.1 (2018-06-11)

First release.
