import json
from collections import defaultdict

json_dict = json.loads(input())

stops_info = defaultdict(set)


def main():
    for element in json_dict:
        for name, value in element.items():
            if name == 'stop_name':
                stops_info[element[name]] |= {element['stop_type']}
    names = [name for name, types in stops_info.items()
             if ('S' in types or 'F' in types or len(types) > 1)
             and ('O' in types)]
    print(f'Wrong stop type: {sorted(names)}' if names else 'OK')


if __name__ == "__main__":
    print('On demand stops test:')
    main()
