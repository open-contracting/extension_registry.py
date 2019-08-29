import json
from collections import OrderedDict


def json_dump(data, io):
    """
    Loads JSON data, preserving order.
    """
    json.dump(data, io, ensure_ascii=False, indent=2, separators=(',', ': '))


def json_loads(data):
    """
    Loads JSON data, preserving order.
    """
    return json.loads(data, object_pairs_hook=OrderedDict)


def add_extension_name(schema, extension_name, pointer=None):
    """
    Sets the extension's name in the `extension` field of all definitions and properties in the schema.
    """
    if pointer is None:
        pointer = ()
    if isinstance(schema, list):
        for item in schema:
            add_extension_name(item, extension_name, pointer=pointer)
    elif isinstance(schema, dict):
        if len(pointer) > 1 and pointer[-2] in ('definitions', 'properties'):
            schema['extension'] = extension_name
        for key, value in schema.items():
            add_extension_name(value, extension_name, pointer=pointer + (key,))
