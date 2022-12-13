from gendiff.utils.format_utils import format_wrong_words, modify_untapped_keys


def stringify(value, char=' ', spaces=1):
    def walk(item, deep_space=0):
        if not isinstance(item, dict):
            return str(item)

        deep_space += spaces
        val_pad = char * deep_space
        bracket_pad = char * (deep_space - spaces)
        strings = [f'{val_pad}{key}: {walk(val, deep_space+3)}\n'
                   for key, val in item.items()]
        strings = str.join("", strings) + bracket_pad
        return '{\n' + strings + '}'
    return walk(value)


def handle_diff(diff):
    modified_diff = dict()
    for key, meta in diff.items():
        status = meta['status']
        values = meta['values']
        if status == 'dicts':
            modified_diff[f'   {key}'] = handle_diff(values)
        elif status == 'equal':
            modified_diff[f'   {key}'] = values
        elif status == 'unequal':
            first, second = values
            modified_diff[f' - {key}'] = first
            modified_diff[f' + {key}'] = second
        else:
            modified_diff[f' {status} {key}'] = values
    modified_diff = modify_untapped_keys(modified_diff)
    return modified_diff


def make_stylish(diff):
    stringifyed = handle_diff(diff)
    stringifyed = stringify(stringifyed)
    stringifyed = format_wrong_words(stringifyed)
    return stringifyed
