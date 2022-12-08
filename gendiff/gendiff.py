def generate_diff(file1: dict, file2: dict):
    keys = {*file2.keys(), *file1.keys()}
    diff_str = ""
    for key in sorted(keys):
        value1 = file1.get(key)
        value2 = file2.get(key)
        if value1 == value2:
            diff_str += f'    {key}: {value2}\n'
        elif value1 is None:
            diff_str += f'  + {key}: {value2}\n'
        elif value2 is None:
            diff_str += f'  - {key}: {value1}\n'
        else:
            diff_str += f'  - {key}: {value1}\n'
            diff_str += f'  + {key}: {value2}\n'
    diff_str = diff_str.replace('True', 'true')
    diff_str = diff_str.replace('False', 'false')
    return '{\n' + diff_str + '}'
