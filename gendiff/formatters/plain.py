from gendiff.utils.format_utils import format_wrong_words


def make_plain(diff):
    plain_diff = str.join('\n', handle_diff(diff))
    plain_diff = format_wrong_words(plain_diff)
    return plain_diff


def handle_diff(diff, parent=None):
    plain_diff = []
    for key, meta in diff.items():
        status, values = meta.values()
        property_name = f'{parent}.{key}' if parent else key
        text = f"Property '{property_name}' was {status}"
        if status == 'added':
            value = format_value(values)
            plain_diff.append(f'{text} with value: {value}')
        elif status == 'removed':
            plain_diff.append(text)
        elif status == 'updated':
            value1, value2 = [format_value(v) for v in values]
            plain_diff.append(f'{text}. From {value1} to {value2}')
        elif status == 'nested':
            plain_diff.extend(handle_diff(values, parent=property_name))
    return plain_diff


def format_value(value):
    complex_types = [type(list()), type(dict())]
    if type(value) in complex_types:
        return '[complex value]'
    elif value == '':
        return "''"
    elif isinstance(value, str):
        return f"'{value}'"
    return value
