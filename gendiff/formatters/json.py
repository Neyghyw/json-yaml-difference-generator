import json
from gendiff.utils.format_utils import format_status


def make_json(diff):
    json_ = handle_diff(diff)
    return json.dumps(json_, indent=4)


def handle_diff(diff):
    new_diff = dict()
    for key, meta in diff.items():
        status, values = meta.values()
        status = format_status(status)
        if status in ['added', 'equal']:
            new_diff[key] = values
        elif status == 'updated':
            _, value = values
            new_diff[key] = value
        elif status == 'dicts':
            new_diff[key] = handle_diff(values)
    return new_diff
