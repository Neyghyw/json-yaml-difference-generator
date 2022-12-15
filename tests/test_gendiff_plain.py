import pytest
from gendiff.modules.gendiff import generate_diff
from gendiff.utils.file_utils import load_yamls


@pytest.fixture
def expected_diff():
    path = f'tests/fixtures/plain_format/expected_diff'
    with open(file=path, mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture
def yaml_files(dir_):
    path1 = f'tests/fixtures/yamls/{dir_}/file1.yaml'
    path2 = f'tests/fixtures/yamls/{dir_}/file2.yaml'
    return load_yamls(path1, path2)


@pytest.mark.parametrize(argvalues=['deep_yamls'], argnames='dir_')
def test_gendiff(yaml_files, expected_diff):
    assert generate_diff(*yaml_files, format_='plain') == expected_diff

