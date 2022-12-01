import json
import pytest
from gendiff.gendiff import generate_diff


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
    json_file1 = json.load(open(file=path1, mode='r'))
    json_file2 = json.load(open(file=path2, mode='r'))
    return json_file1, json_file2


def test_gendiff(json_files, expected):
    assert generate_diff(*json_files) == expected
