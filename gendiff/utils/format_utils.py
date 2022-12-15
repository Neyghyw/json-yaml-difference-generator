def format_wrong_words(value: str):
    value = value.replace('True', 'true')
    value = value.replace('False', 'false')
    value = value.replace('None', 'null')
    value = value.replace(': \n', ':\n')
    return value
