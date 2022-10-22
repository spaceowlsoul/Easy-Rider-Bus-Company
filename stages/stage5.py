import json
from collections import defaultdict

json_dict = json.loads(input())

lines_info = defaultdict(list)


def main():
    for element in json_dict:
        for name, value in element.items():
            if name == 'bus_id':
                lines_info[element[name]].append((element['stop_id'], element['stop_name'], element['a_time']))
    wrong_time = 0
    for line, info in lines_info.items():
        for i in range(1, len(info)):
            if info[i][2] < info[i - 1][2]:
                wrong_time += 1
                print(f'bus_id line {line}: wrong time on station {info[i][1]}')
                break
    if wrong_time == 0:
        print('OK')


if __name__ == "__main__":
    print('Arrival time test:')
    main()
