#!/usr/bin/python3
import argparse
from gendiff.lib.gendiff import generate_diff


def main():
    parser_params = {
        'prog': 'gendiff',
        'usage': 'gendiff [-h] [-f FORMAT] first_file second_file',
        'description': 'Compares two configuration '
                       'files and shows a difference.',
        'epilog': 'Supported files extensions: json, yaml or yml.'
    }
    parser = argparse.ArgumentParser(**parser_params)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish', required=False,
                        choices=['json', 'stylish', 'plain'])
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
