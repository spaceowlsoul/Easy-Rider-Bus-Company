import json
from collections import defaultdict

json_dict = json.loads(input())

stop_name_lines = defaultdict(set)
line_stop_types = defaultdict(set)
stop_name_types = []


def main():
    for element in json_dict:
        for name, value in element.items():
            if name == 'bus_id':
                stop_name_lines[element['stop_name']] |= {value}
                line_stop_types[element[name]] |= {element['stop_type']}
                stop_name_types.append((element['stop_name'], element['stop_type']))
    start_end_check()


def start_end_check():
    error = 0
    for line, stops in line_stop_types.items():
        if 'S' not in stops or 'F' not in stops:
            print(f'There is no start or end stop for the line: {line}.')
            error += 1
    if error == 0:
        output_stops()


def output_stops():
    start_stops = {stop[0] for stop in stop_name_types if stop[1] == 'S'}
    end_stops = {stop[0] for stop in stop_name_types if stop[1] == 'F'}
    transfer_stops = [stop_name for stop_name, lines in
                      stop_name_lines.items() if len(lines) > 1]
    print(f'Start stops: {len(start_stops)} {sorted(start_stops)}')
    print(f'Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}')
    print(f'Finish stops: {len(end_stops)} {sorted(end_stops)}')


if __name__ == "__main__":
    main()
