from gendiff.formatters import formatters_map
from gendiff.utils.file_utils import handle_paths, get_dicts_from_files


def make_key_map(table, dict1, dict2):
    keys = sorted({*dict1.keys(), *dict2.keys()})
    for key in keys:
        items = []
        if key in dict1.keys():
            items.append(dict1[key])
        if key in dict2.keys():
            items.append(dict2[key])
        table[key] = items


def create_diff(dict1, dict2):
    diff = dict()
    key_map = dict()
    make_key_map(key_map, dict1, dict2)
    for key, values in key_map.items():
        if len(values) == 1:
            status = '-' if key in dict1.keys() \
                else '+'
            values = values[0]
        else:
            first, second = values
            if isinstance(first, dict) and isinstance(second, dict):
                status = 'dicts'
                values = create_diff(first, second)
            elif first == second:
                status = 'equal'
                values = first
            else:
                status = 'unequal'
                values = first, second
        diff[key] = {'status': status, 'values': values}
    return diff


def generate_diff(path1, path2, format_='stylish'):
    paths = handle_paths(path1, path2)
    dicts = get_dicts_from_files(*paths)
    diff = create_diff(*dicts)
    formatter = formatters_map.get(format_, 'stylish')
    formatted_diff = formatter(diff)
    return formatted_diff
