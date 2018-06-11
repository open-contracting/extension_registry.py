from ocdsextensionregistry import Extension, ExtensionVersion


def test_init():
    args = arguments()
    obj = ExtensionVersion(args)

    assert obj.id == args['Id']
    assert obj.date == args['Date']
    assert obj.version == args['Version']
    assert obj.base_url == args['Base URL']
    assert obj.download_url == args['Download URL']


def test_update():
    obj = ExtensionVersion(arguments())
    obj.update(Extension({'Id': 'location', 'Category': 'item', 'Core': 'true'}))

    assert obj.id == 'location'
    assert obj.category == 'item'
    assert obj.core is True


def test_metadata():
    obj = ExtensionVersion(arguments())
    result = obj.metadata

    assert 'name' in result
    assert 'description' in result


def test_repository_full_name():
    obj = ExtensionVersion(arguments())
    result = obj.repository_full_name

    assert result == 'open-contracting/ocds_location_extension'


def test_repository_name():
    obj = ExtensionVersion(arguments())
    result = obj.repository_name

    assert result == 'ocds_location_extension'


def test_repository_html_page():
    obj = ExtensionVersion(arguments())
    result = obj.repository_html_page

    assert result == 'https://github.com/open-contracting/ocds_location_extension'


def test_repository_url():
    obj = ExtensionVersion(arguments())
    result = obj.repository_url

    assert result == 'git@github.com:open-contracting/ocds_location_extension.git'


def arguments(**kwargs):
    data = {
        'Id': 'location',
        'Date': '2018-02-01',
        'Version': 'v1.1.3',
        'Base URL': 'https://raw.githubusercontent.com/open-contracting/ocds_location_extension/v1.1.3/',
        'Download URL': 'https://api.github.com/repos/open-contracting/ocds_location_extension/zipball/v1.1.3',
    }

    data.update(kwargs)
    return data
