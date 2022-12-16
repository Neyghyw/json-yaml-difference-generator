def format_wrong_words(value: str):
    value = value.replace('True', 'true')
    value = value.replace('False', 'false')
    value = value.replace('None', 'null')
    return value


def format_status(status):
    if status == '+':
        return 'added'
    if status == '-':
        return 'removed'
    if status == 'unequal':
        return 'updated'
    return status
