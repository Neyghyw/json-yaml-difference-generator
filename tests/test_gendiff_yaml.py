import pytest
from gendiff.gendiff import generate_diff
from gendiff.utils import load_yamls


@pytest.fixture
def yaml_expected(dir_):
    path = f'tests/fixtures/yamls/{dir_}/expected_diff'
    with open(file=path, mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture
def yaml_files(dir_):
    path1 = f'tests/fixtures/yamls/{dir_}/file1.yaml'
    path2 = f'tests/fixtures/yamls/{dir_}/file2.yaml'
    return load_yamls(path1, path2)


@pytest.mark.parametrize(argvalues=['simple_yamls', 'deep_yamls'], argnames='dir_')
def test_gendiff(yaml_files, yaml_expected):
    assert generate_diff(*yaml_files) == yaml_expected

