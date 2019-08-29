Codelist
========

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

API
---

.. autoclass:: ocdsextensionregistry.codelist.Codelist
    :special-members:
    :exclude-members: __weakref__
