from .formatters.stylish import make_stylish
from .utils.from_format.utils import format_wrong_words
from .utils.from_format.utils import modify_untapped_keys


def make_keymap(table, dict1, dict2):
    keys = sorted({*dict1.keys(), *dict2.keys()})
    for key in keys:
        items = []
        if key in dict1.keys():
            items.append(dict1[key])
        if key in dict2.keys():
            items.append(dict2[key])
        table[key] = items


def generate_diff(dict1, dict2):
    diff = dict()
    key_map = dict()
    make_keymap(key_map, dict1, dict2)

    for key, values in key_map.items():
        if len(values) == 1:
            mark = '-' if key in dict1.keys() else '+'
            value = values[0]
            diff[f' {mark} {key}'] = value
        else:
            first, second = values
            if isinstance(first, dict) and isinstance(second, dict):
                diff[f'   {key}'] = generate_diff(first, second)
            elif first == second:
                diff[f'   {key}'] = first
            else:
                diff[f' - {key}'] = first
                diff[f' + {key}'] = second
    return diff


def stringify(diff: dict):
    diff = modify_untapped_keys(diff)
    stringifyed = make_stylish(diff)
    stringifyed = format_wrong_words(stringifyed)
    return stringifyed
