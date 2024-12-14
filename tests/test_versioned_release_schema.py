import json

from ocdsextensionregistry import get_versioned_release_schema
from tests import read


def test_get_versioned_release_schema():
    schema = get_versioned_release_schema(json.loads(read('release-schema.json')), '1__1__5')

    assert schema == json.loads(read('versioned-release-validation-schema.json'))
