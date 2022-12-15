from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json

formatters_map = {
    'stylish': make_stylish,
    'plain': make_plain,
    'json': make_json
}
