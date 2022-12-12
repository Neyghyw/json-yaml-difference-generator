from .formatters.stylish import make_stylish
from .utils.from_format.utils import replace_unsuitable


def generate_diff(file1: dict, file2: dict):
    diff_dict = dict()
    fields = sorted({*file2.keys(), *file1.keys()})

    def walk(key):
        value1 = file1.get(key, 'netu')
        value2 = file2.get(key, 'netu')
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff_dict[f'   {key}'] = generate_diff(value1, value2)
        elif isinstance(value1, dict):
            diff_dict[f' - {key}'] = generate_diff(value1, value1)
            if value2 != 'netu':
                diff_dict[f' + {key}'] = value2
        elif isinstance(value2, dict):
            if value1 != 'netu':
                diff_dict[f' - {key}'] = value1
            diff_dict[f' + {key}'] = generate_diff(value2, value2)
        elif value1 == value2:
            diff_dict[f'   {key}'] = value1
        elif value1 == 'netu':
            diff_dict[f' + {key}'] = value2
        elif value2 == 'netu':
            diff_dict[f' - {key}'] = value1
        else:
            diff_dict[f' - {key}'] = value1
            diff_dict[f' + {key}'] = value2
    for field in fields:
        walk(field)
    return diff_dict


def stringify(diff: dict):
    result = make_stylish(diff)
    return replace_unsuitable(result)
