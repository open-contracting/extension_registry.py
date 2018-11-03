Translation
===========

Setup
-----

Install this package with command-line tools as well as ``sphinx-intl`` and ``transifex-client``::

    pip install ocdsextensionregistry[cli] 'sphinx-intl<1' transifex-client

Create a `~/.transifexrc <https://docs.transifex.com/client/client-configuration#%7E/-transifexrc>`__ file (replace ``USERNAME`` and ``PASSWORD``)::

    sphinx-intl create-transifexrc --transifex-username USERNAME --transifex-password PASSWORD

Create new translations
-----------------------

Create a project on Transifex (in this example, our project's identifier is ``ocds-extensions``). You might want to `upload <https://docs.transifex.com/setup/glossary/uploading-an-existing-glossary>`__ the `OCDS glossary <https://github.com/open-contracting/glossary/tree/master/glossaries>`__ in your language to Transifex, to assist with translation.

Generate POT files for all versions of all extensions::

    ocdsextensionregistry generate-pot-files build/locale

Or, generate POT files for the versions of extensions you want to translate, for example::

    ocdsextensionregistry generate-pot-files build/locale lots bids==v1.1.3

Remove any existing ``.tx/config`` file::

    rm -f .tx/config

Create a new ``.tx/config`` file::

    sphinx-intl create-txconfig

Update the ``.tx/config`` file based on the POT files (replace ``ocds-extensions`` with your Transifex project)::

    sphinx-intl update-txconfig-resources --transifex-project-name ocds-extensions --pot-dir build/locale --locale-dir locale

Push source files to Transifex for translation::

    tx push -s

Once you've translated strings on Transifex, email <data@open-contracting.org> so that we can pull translation files from Transifex::

    tx pull -a -f

Update existing translations
----------------------------

Existing translations are stored in `ocds-extensions-translations <https://github.com/open-contracting/ocds-extensions-translations>`__.

Follow the steps for creating new translations, then clone the repository::

    git clone https://github.com/open-contracting/ocds-extensions-translations.git

And push its translations::

    tx push -t

See `Transifex's documentation <https://docs.transifex.com/client/push>`__ for more information on how to specify which languages or resources to push.