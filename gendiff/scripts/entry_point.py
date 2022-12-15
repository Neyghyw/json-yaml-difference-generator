#!/usr/bin/python3
import argparse
from gendiff.modules.gendiff import generate_diff


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
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
