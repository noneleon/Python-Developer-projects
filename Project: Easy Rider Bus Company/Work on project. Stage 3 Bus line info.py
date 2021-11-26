'''
Description
It wasn't easy, but finally, you verified the data format and the required fields. It is now time to check how many bus lines we have and how many stops there are on each line. Before we can go further with sorting out the database, it would be a good idea to check that the information is complete.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Find the names of all the bus lines.
Verify the number of stops for each line.
The output should have the same formatting as shown in the example.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Example
Input:

[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
Output:

Line names and number of stops:
bus_id: 128, stops: 4
bus_id: 256, stops: 4
bus_id: 512, stops: 2
'''
import json


def stops(json_final):
    lines = {}
    for x in json_final:
        try:
            lines[x["bus_id"]].append(x)
        except KeyError:
            lines[x["bus_id"]] = [x]
    return lines


def stage_3(json_final):
    print("Line names and number of stops:")
    lines = stops(json_final)
    for x in lines:
        print(f"bus_id: {x}, stops: {len(lines[x])}")
    pass


easy_rider = json.loads(input())
stage_3(easy_rider)

\\
import json
import re

valid = {
    "bus_id": {"required": True, "type": int},
    "stop_id": {"required": True, "type": int},
    "stop_name": {"required": True, "type": str, "suffix": ("Road", "Avenue", "Boulevard", "Street")},
    "next_stop": {"required": True, "type": int},
    "stop_type": {"required": False, "type": str, "in": ("S", "O", "F")},
    "a_time": {"required": True, "type": str, "time": True}
}

# errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
errors = {"stop_name": 0, "stop_type": 0, "a_time": 0}
bus_ids = {}


def process():
    # json_string = json.dumps(json_data)
    json_string = input()
    prepare(json.loads(json_string))
    # prepare_errors()
    prepare_bus_ids()


def prepare(data: list):
    for row in data:
        prepare_row(row)
        bus_id = row.get("bus_id")
        stop_id = row.get("stop_id")
        if bus_id not in bus_ids.keys():
            bus_ids[bus_id] = {"stops": []}
        if stop_id not in bus_ids[bus_id]["stops"]:
            bus_ids[bus_id]["stops"].append(stop_id)


def prepare_row(row: dict):
    for key, val in row.items():
        validate(key, val)


def validate(key: str, val):
    valid_data = valid[key]
    if valid_data["required"] is True and not val and val != 0:
        errors[key] += 1
    elif val and type(val) is not valid_data["type"]:
        errors[key] += 1
    elif val and valid_data["type"] == str and "in" in valid_data.keys() and val not in valid_data["in"]:
        errors[key] += 1
    elif val and valid_data["type"] == str and "suffix" in valid_data.keys():
        template = r"(.*[A-Z]{1}\w+.*) (" + "|".join(valid_data['suffix']) + ")$"
        res = re.findall(template, val)
        if len(res) == 0:
            errors[key] += 1
    elif val and valid_data["type"] == str and "suffix" in valid_data.keys() and val[0].islower():
        errors[key] += 1
    elif val and valid_data["type"] == str and "time" in valid_data.keys():
        template = r"(0[0-9]|1[0-9]|2[0-4]):([0-5][0-9])$"
        math = re.match(template, val)
        if math is None:
            errors[key] += 1


def prepare_errors():
    sum_errors = sum(errors.values())
    print(f"Type and required field validation: {sum_errors} errors")
    for key, val in errors.items():
        if val == 0 and sum_errors > 0:
            continue
        print(f"{key}: {val}")


def prepare_bus_ids():
    print(f"Line names and number of stops:")
    for key, val in bus_ids.items():
        stops = val.get("stops")
        if stops and len(stops) > 0:
            print(f"bus_id: {key}, stops: {len(stops)}")


process()
\\
# Write your awesome code here
import json
from typing import Dict, List
from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict


def stop_count(data: List[Dict]) -> Dict[int, int]:
    result: Dict[int, set] = defaultdict(set)
    for i in data:
        result[i['bus_id']].add(i['stop_name'])
    return {i: len(j) for i, j in result.items()}


def check_existence_and_type(data: dict) -> Dict[str, int]:
    errors: Dict[str, int] = {}
    for field, value in data.items():
        if field in ('bus_id', 'stop_id', 'next_stop'):
            if not isinstance(value, int):
                # errors[field] = errors.get(field, 0) + 1
                pass
        elif field in ('stop_name', 'a_time'):
            if (not isinstance(value, str)) or value == '':
                errors[field] = errors.get(field, 0) + 1
            elif field == 'a_time':
                if value.count(':') != 1:
                    errors[field] = errors.get(field, 0) + 1
                    continue
                hour, minute = value.split(':')
                if len(hour) != 2 or len(minute) != 2:
                    errors[field] = errors.get(field, 0) + 1
                    continue
                hour, minute = int(hour), int(minute)
                if hour > 24 or minute > 60 or (hour == 24 and minute != 0):
                    errors[field] = errors.get(field, 0) + 1
                    continue
            elif field == 'stop_name':
                if value[0] not in ascii_uppercase:
                    errors[field] = errors.get(field, 0) + 1
                    continue
                if len(value.split()) < 2:
                    errors[field] = errors.get(field, 0) + 1
                    continue
                if value.split()[-1] not in ('Road', 'Avenue', 'Boulevard', 'Street'):
                    errors[field] = errors.get(field, 0) + 1
                    continue
        elif field == 'stop_type':
            if not isinstance(value, str):
                errors[field] = errors.get(field, 0) + 1
            elif len(value) > 1 or value not in 'SOF':
                errors[field] = errors.get(field, 0) + 1
    return errors


# Input data
data = input()
data = json.loads(data)

# Check existence
errors = {
    # 'bus_id': 0,
    # 'stop_id': 0,
    'stop_name': 0,
    # 'next_stop': 0,
    'stop_type': 0,
    'a_time': 0
}
# for i in data:
#     i_errors = check_existence_and_type(i)
#     for j in i_errors:
#         errors[j] += i_errors[j]

# Output
# number_of_errors = sum(errors.values())
# print(f'Type and required field validation: {number_of_errors} errors')
# print(f'Format validation: {number_of_errors} errors')
# for field, n in errors.items():
#     print(f'{field}:', n)


# Output
print('Line names and number of stops:')
for bus, n in stop_count(data).items():
    print(f'bus_id: {bus}, stope: {n}')


