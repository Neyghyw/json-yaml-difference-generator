import json


def load_jsons(*args):
    try:
        jsons = [json.load(open(file=path, mode='r')) for path in args]
    except Exception as ex:
        raise ImportError(ex)
    return jsons
