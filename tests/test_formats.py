import pytest
from gendiff.lib.gendiff import generate_diff


@pytest.fixture
def expected_diff(format_):
    path = f'tests/fixtures/{format_}/expected_diff'
    with open(file=path, mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture
def paths(type_):
    path1 = f'tests/fixtures/file1.{type_}'
    path2 = f'tests/fixtures/file2.{type_}'
    return path1, path2


@pytest.mark.parametrize(argvalues=['json', 'plain', 'stylish'], argnames='format_')
@pytest.mark.parametrize(argvalues=['json', 'yaml'], argnames='type_')
def test_gendiff(paths, expected_diff, format_):
    print(generate_diff(*paths, format_=format_))
    assert generate_diff(*paths, format_=format_) == expected_diff
