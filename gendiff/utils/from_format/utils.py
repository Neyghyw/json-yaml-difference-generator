def format_wrong_words(value: str):
    value = value.replace('True', 'true')
    value = value.replace('False', 'false')
    value = value.replace('None', 'null')
    value = value.replace(': \n', ':\n')
    return value


def is_key_untapped(key: str):
    is_tapped = key.startswith(' + ')
    is_tapped |= key.startswith(' - ')
    is_tapped |= key.startswith('   ')
    if is_tapped:
        return False
    return True


def modify_untapped_keys(dict_: dict):
    keys = list(dict_.keys())
    values = list(dict_.values())
    for index, key in enumerate(keys[:]):
        if is_key_untapped(key):
            keys[index] = f'   {key}'

    for index, val in enumerate(values[:]):
        if isinstance(val, dict):
            values[index] = modify_untapped_keys(val)
    modified_dict = {key: value for key, value in zip(keys, values)}
    return modified_dict
