#!/usr/bin/python3
import argparse
from gendiff.modules.gendiff import generate_diff, stringify
from gendiff.utils.file_utils import handle_files
from gendiff.utils.file_utils import handle_paths


def main():
    parser_params = {
        'prog': 'gendiff',
        'usage': 'gendiff [-h] [-f FORMAT] first_file second_file',
        'description': 'Compares two configuration files and shows a difference.'  # noqa: E501
    }
    parser = argparse.ArgumentParser(**parser_params)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish', required=False)  # noqa: E501
    args = parser.parse_args()
    paths = handle_paths(args.first_file, args.second_file)
    dicts = handle_files(*paths)
    diff = generate_diff(*dicts)
    print(stringify(diff))


if __name__ == '__main__':
    main()
