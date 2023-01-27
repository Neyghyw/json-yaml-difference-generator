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
        content = file.read()
        return content, extension


def parse_content(content, extension):
    try:
        if extension == '.json':
            return json.loads(content)
        elif extension in ['.yaml', '.yml']:
            return yaml.load(content, Loader)
        else:
            raise 'Unsupported file.'
    except Exception as ex:
        raise ImportError(ex)


def handle_paths(*args):
    handled_paths = list(args)
    for index, path in enumerate(args):
        if not exists(path):
            handled_paths[index] = os.getcwd() + '/' + path
    return handled_paths
