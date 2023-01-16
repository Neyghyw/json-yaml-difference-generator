from gendiff.utils.format_utils import format_wrong_words

INDENT = 4
status_map = {'added': '+', 'removed': '-'}


def make_stylish(diff):
    stringifyed = stringify(diff, is_diff=True)
    return format_wrong_words(stringifyed)


def stringify(item, spaces=0, is_diff=False, barchar=' '):
    if not isinstance(item, dict):
        return str(item)

    bracket_pad = barchar * spaces
    pad = barchar * (spaces + 1)

    if not is_diff:
        strings = [f'{pad}   {key}: {stringify(val, spaces + INDENT)}\n'
                   for key, val in item.items()]
    else:
        strings = []
        for key, meta in item.items():
            status = meta['status']
            value = meta['value']
            if status == 'updated':
                first, second = [stringify(v, spaces + INDENT) for v in value]
                strings += f'{pad} - {key}: {first}\n' \
                           f'{pad} + {key}: {second}\n'
            else:
                is_nested = status == 'nested'
                status = status_map.get(status, barchar)
                value = stringify(value, spaces + INDENT, is_nested)
                strings += f'{pad} {status} {key}: {value}\n'
    strings = str.join('', strings) + bracket_pad
    return '{\n' + strings + '}'
