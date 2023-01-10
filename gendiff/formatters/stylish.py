from gendiff.utils.format_utils import format_wrong_words


def make_stylish(diff):
    stringifyed = stringify(diff, is_diff=True)
    return format_wrong_words(stringifyed)


def stringify(item, spaces=0, is_diff=False, barchar=' '):
    if not isinstance(item, dict):
        return str(item)

    bracket_pad = barchar * spaces
    pad = barchar * (spaces + 1)

    if not is_diff:
        strings = [f'{pad}   {key}: {stringify(val, spaces + 4)}\n'
                   for key, val in item.items()]
    else:
        strings = []
        for key, meta in item.items():
            status = meta['status']
            value = meta['values']
            if status == 'unequal':
                first, second = [stringify(val, spaces + 4) for val in value]
                strings += f'{pad} - {key}: {first}\n' \
                           f'{pad} + {key}: {second}\n'
            else:
                is_dicts = status == 'dicts'
                value = stringify(value, spaces + 4, is_dicts)
                status = status if status in ['-', '+'] else barchar
                strings += f'{pad} {status} {key}: {value}\n'
    strings = str.join("", strings) + bracket_pad
    return '{\n' + strings + '}'
