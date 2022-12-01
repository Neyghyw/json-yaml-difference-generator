import pytest
from gendiff.gendiff import generate_diff
from utils import load_jsons


@pytest.fixture()
def expected():
    with open('./fixtures/expected_diff', mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture()
def json_files():
    path1 = './fixtures/file1.json'
    path2 = './fixtures/file2.json'
    return load_jsons(path1, path2)


def test_gendiff(json_files, expected):
    assert generate_diff(*json_files) == expected
