import pytest
from gendiff.gendiff import generate_diff
from gendiff.utils import load_yamls


@pytest.fixture()
def expected():
    with open('tests/fixtures/yamls/expected_diff', mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture()
def yaml_files():
    path1 = 'tests/fixtures/yamls/file1.yaml'
    path2 = 'tests/fixtures/yamls/file2.yaml'
    return load_yamls(path1, path2)


def test_gendiff(yaml_files, expected):
    assert generate_diff(*yaml_files) == expected
