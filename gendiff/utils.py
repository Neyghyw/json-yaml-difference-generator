import json
import yaml
import re
from yaml import CLoader as Loader


def load_dicts_from_files(*args):
    paths = str.join('\n', args)
    extensions = re.findall(r'(?<=\.)json|(?<=ya)ml|(?<=y)ml$', paths)
    if len(extensions) <= 1:
        raise ImportError('Unknown file extension.')

    extensions = set(extensions)
    if len(extensions) > 1:
        raise ImportError('Incompatible files extensions.')
    elif extensions.intersection('json') == json:
        return load_jsons(*args)
    else:
        return load_yamls(*args)


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
