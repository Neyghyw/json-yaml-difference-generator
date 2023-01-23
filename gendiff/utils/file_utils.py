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
        return content


def parse_content(content):
    try:
        if is_json(content):
            return json.loads(content)
        elif is_yaml(content):
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


def is_json(content):
    try:
        json.loads(content)
    except ValueError:
        return False
    return True


def is_yaml(content):
    try:
        yaml.load(content, Loader)
    except ValueError:
        return False
    return True
