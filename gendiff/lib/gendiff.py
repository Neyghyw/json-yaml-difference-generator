from gendiff.formatters import formatters_map
from gendiff.utils.file_utils import handle_paths, get_dicts_from_files


def create_diff(dict1, dict2):
    diff = dict()
    sorted_keys = sorted({*dict1.keys(), *dict2.keys()})
    for key in sorted_keys:
        values = [table[key] for table in [dict1, dict2] if key in table]
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
