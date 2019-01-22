|PyPI Version| |Build Status| |Coverage Status| |Python Version|

This Python package eases access to information about extensions in the `Open Contracting Data Standard <http://standard.open-contracting.org>`__'s `extension registry <https://github.com/open-contracting/extension_registry>`__.

It includes Python classes for programmatic access, as well as a suite of command-line tools which can:

* download any versions of extensions
* generate POT files (message catalogs) from extension files, as part of a translation worlflow
* generate a data file in JSON format, that provides all the information about versions of extensions

The command-line tools have additional requirements, including Sphinx. To install without command-line tools::

    pip install ocdsextensionregistry

To install with command-line tools::

    pip install ocdsextensionregistry[cli]
    pip install -e git+https://github.com/rtfd/recommonmark.git@81d7c6f7b37981ac22571dd91a7cc9d24c3e66a1#egg=recommonmark

To see all commands available, run::

    ocdsextensionregistry --help

If you are viewing this on GitHub or PyPi, open the `full documentation <https://ocdsextensionregistry.readthedocs.io/>`__ for additional details.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/ocdsextensionregistry.svg
   :target: https://pypi.org/project/ocdsextensionregistry/
.. |Build Status| image:: https://secure.travis-ci.org/open-contracting/extension_registry.py.png
   :target: https://travis-ci.org/open-contracting/extension_registry.py
.. |Coverage Status| image:: https://coveralls.io/repos/github/open-contracting/extension_registry.py/badge.png?branch=master
   :target: https://coveralls.io/github/open-contracting/extension_registry.py?branch=master
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/ocdsextensionregistry.svg
   :target: https://pypi.org/project/ocdsextensionregistry/
