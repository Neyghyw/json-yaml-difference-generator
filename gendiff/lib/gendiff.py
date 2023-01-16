from gendiff.formatters import formatters_map
from gendiff.utils.file_utils import handle_paths, load_content


def create_diff(dict1, dict2):
    diff = dict()
    sorted_keys = sorted({*dict1.keys(), *dict2.keys()})
    for key in sorted_keys:
        value = [table[key] for table in [dict1, dict2] if key in table]
        if len(value) == 1:
            status = 'removed' if key in dict1.keys() \
                else 'added'
            value = value[0]
        else:
            first, second = value
            if isinstance(first, dict) and isinstance(second, dict):
                status = 'nested'
                value = create_diff(first, second)
            elif first == second:
                status = 'equal'
                value = first
            else:
                status = 'updated'
                value = first, second
        diff[key] = {'status': status, 'value': value}
    return diff


def generate_diff(path1, path2, format_='stylish'):
    paths = handle_paths(path1, path2)
    dicts = [load_content(path) for path in paths]
    diff = create_diff(*dicts)
    formatter = formatters_map.get(format_, 'stylish')
    formatted_diff = formatter(diff)
    return formatted_diff
