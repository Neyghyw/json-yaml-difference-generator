import json
import os
import yaml
from os.path import exists, splitext

from yaml import CLoader as Loader


def load_content(path):
    extension = splitext(path)[-1]
    if extension not in ['.json', '.yml', '.yaml']:
        raise ImportError(f'File {path} had unsupported extension.')
    with open(path) as file:
        return parse_file(file, extension)


def parse_file(file, extension):
    try:
        if extension == '.json':
            return json.load(file)
        elif extension in ['.yml', '.yaml']:
            return yaml.load(file, Loader)
    except Exception as ex:
        raise ImportError(ex)


def handle_paths(*args):
    handled_paths = list(args)
    for index, path in enumerate(args):
        if not exists(path):
            handled_paths[index] = os.getcwd() + '/' + path
    return handled_paths
