#!/usr/bin/python3
import argparse
from ..gendiff import generate_diff
from ..utils import load_jsons


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     usage='gendiff [-h] [-f FORMAT] first_file second_file',
                                     description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', required=False)
    args = parser.parse_args()
    jsons = load_jsons(args.first_file, args.second_file)
    print(generate_diff(*jsons))


if __name__ == '__main__':
    main()
