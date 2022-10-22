import json
import re

data = input()
json_dict = json.loads(data)
errors = {key: 0 for key in json_dict[0].keys()}


def main():
    for d in json_dict:
        for k, v in d.items():
            if k == 'stop_name':
                if re.match('([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$', v) is None:
                    errors[k] += 1
            elif k == 'stop_type':
                if re.match(r'^[SOF]?$', v) is None:
                    errors[k] += 1
            elif k == 'a_time':
                if re.match('^([01][0-9]|2[0-4]):([0-5][0-9])$', v) is None:
                    errors[k] += 1
    print(f'Type and required field validation: {sum(errors.values())} errors')
    for k, v in errors.items():
        if k in ('stop_name', 'stop_type', 'a_time'):
            print(f'{k}: {v}')
