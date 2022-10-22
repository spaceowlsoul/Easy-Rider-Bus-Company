import json

data = input()
json_dict = json.loads(data)
errors = {key: 0 for key in json_dict[0].keys()}


def main():
    for d in json_dict:
        for k, v in d.items():
            if k in ('stop_id', 'bus_id', 'next_stop'):
                if not isinstance(v, int) or v == '':
                    errors[k] += 1
            elif k in ('stop_name', 'a_time'):
                if not isinstance(v, str) or v == '':
                    errors[k] += 1
            elif k == 'stop_type':
                if not isinstance(v, str) or len(v) > 1:
                    errors[k] += 1
    print(f'Type and required field validation: {sum(errors.values())} errors')
    for k, v in errors.items():
        print(f'{k}: {v}')


if __name__ == "__main__":
    main()
