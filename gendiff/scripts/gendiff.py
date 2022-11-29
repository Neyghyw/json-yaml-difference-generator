#!/usr/bin/python3
import argparse


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     usage='gendiff [-h] [-f FORMAT] first_file second_file',
                                     description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', required=False)
    parser.parse_args()


if __name__ == '__main__':
    main()
