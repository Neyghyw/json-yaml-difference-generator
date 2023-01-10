import json
import yaml
import os
from os.path import exists
from yaml import CLoader as Loader


def get_dicts_from_files(*args):
    extensions = [path.split('.')[-1] for path in args]
    if len(extensions) <= 1:
        raise ImportError('Unknown file extension.')
    elif len(set(extensions)) > 1 and set(extensions) != {'yml', 'yaml'}:
        raise ImportError('Incompatible files extensions.')

    elif 'json' in extensions:
        return load_jsons(*args)
    elif 'yaml' in extensions \
            or 'yml' in extensions:
        return load_yamls(*args)
    else:
        raise ImportError(f'{extensions} is unsupported file format(s).')


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
