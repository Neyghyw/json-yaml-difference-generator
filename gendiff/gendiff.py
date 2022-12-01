def generate_diff(file1: dict, file2: dict):
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    keys = sorted(set(keys1 + keys2))
    diff_str = ""
    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if value1 in [True, False]:
            value1 = str(value1).lower()
        if value2 in [True, False]:
            value2 = str(value2).lower()
        if value1 == value2:
            diff_str += f'    {key}: {value1}\n'
        elif value1 is None:
            diff_str += f'  + {key}: {value2}\n'
        elif value2 is None:
            diff_str += f'  - {key}: {value1}\n'
        else:
            diff_str += f'  - {key}: {value1}\n'
            diff_str += f'  + {key}: {value2}\n'
    return '{\n' + diff_str + '}'
