import json
from pprint import pprint


def make_json(diff):
    return json.dumps(diff, indent=4)
