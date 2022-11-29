#!/usr/bin/python3
import argparse


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     usage='gendiff [-h] first_file second_file',
                                     description='Compares two configuration files and shows a difference.',
                                     epilog='show this help message and exit')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.parse_args()


if __name__ == '__main__':
    main()
