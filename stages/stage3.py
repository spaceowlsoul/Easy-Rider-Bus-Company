import json

data = input()
json_dict = json.loads(data)
stops = {}


def main():
    for d in json_dict:
        for k, v in d.items():
            if k == 'bus_id':
                stops.setdefault(v, 0)
                stops[v] += 1
    print('Line names and number of stops:')
    for id_, total_ in stops.items():
        print(f'bus_id: {id_}, stops: {total_}')


if __name__ == "__main__":
    main()
