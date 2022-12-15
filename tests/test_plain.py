import pytest
from gendiff.modules.gendiff import generate_diff
from gendiff.utils.file_utils import load_yamls
from gendiff.utils.file_utils import load_jsons


@pytest.fixture
def expected_diff():
    path = f'tests/fixtures/plain/expected_diff'
    with open(file=path, mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture
def dicts(type_):
    path1 = f'tests/fixtures/file1.{type_}'
    path2 = f'tests/fixtures/file2.{type_}'
    if type_ == 'json':
        return load_jsons(path1, path2)
    return load_yamls(path1, path2)


@pytest.mark.parametrize(argvalues=['json', 'yaml'], argnames='type_')
def test_gendiff(dicts, expected_diff):
    assert generate_diff(*dicts, format_='plain') == expected_diff