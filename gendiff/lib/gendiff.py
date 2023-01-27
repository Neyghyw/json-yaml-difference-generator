from gendiff.formatters import formatters_map
from gendiff.utils.file_utils import handle_paths, load_content, parse_content


def create_diff(dict1, dict2):
    diff = dict()
    sorted_keys = sorted({*dict1.keys(), *dict2.keys()})
    for key in sorted_keys:
        if key in dict1 and key in dict2:
            first, second = dict1[key], dict2[key]
            if isinstance(first, dict) and isinstance(second, dict):
                status = 'nested'
                value = create_diff(first, second)
            elif first == second:
                status = 'equal'
                value = first
            else:
                status = 'updated'
                value = first, second
        elif key in dict1.keys():
            status = 'removed'
            value = dict1[key]
        else:
            status = 'added'
            value = dict2[key]
        diff[key] = {'status': status, 'value': value}
    return diff


def generate_diff(path1, path2, format_='stylish'):
    paths = handle_paths(path1, path2)
    contents = [load_content(path) for path in paths]
    dicts = [parse_content(*content) for content in contents]
    diff = create_diff(*dicts)
    formatter = formatters_map.get(format_, 'stylish')
    formatted_diff = formatter(diff)
    return formatted_diff
