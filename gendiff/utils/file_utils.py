import json
import yaml
import re
import os
from os.path import exists
from yaml import CLoader as Loader


def get_dicts_from_files(*args):
    paths = str.join('\n', args)
    extension_regular = r'(?<=\.)json|(?<=ya)ml|(?<=y)ml'
    extensions = re.findall(extension_regular, paths)
    if len(extensions) <= 1:
        raise ImportError('Unknown file extension.')
    elif len(set(extensions)) > 1:
        raise ImportError('Incompatible files extensions.')

    elif 'json' in extensions:
        return load_jsons(*args)
    return load_yamls(*args)


def handle_paths(*args):
    handled_paths = list(args)
    for index, path in enumerate(args):
        if not exists(path):
            handled_paths[index] = os.getcwd() + '/' + path
    return handled_paths


def load_jsons(*args):
    try:
        jsons = [json.load(open(file=path, mode='r')) for path in args]
        return jsons
    except Exception as ex:
        raise ImportError(ex)


def load_yamls(*args):
    try:
        yamls = [yaml.load(open(file=path, mode='r'), Loader) for path in args]
        return yamls
    except Exception as ex:
        raise ImportError(ex)
