def make_stylish(value, char=' ', spaces=1):
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
