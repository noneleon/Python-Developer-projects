'''
Description
You managed to fill in all the missing data and correct the mistakes with the types. However, you noticed that there are multiple problems with suffix names for the stops: sometimes they are incorrect, and sometimes they are simply missing. As if that was not enough, you also realized that there are errors in the arrival times.

It seems like you have to carefully look at the entire "Format" column in the first part of the documentation.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Check that the data format complies with the documentation.
Only the fields that have such a requirement are relevant.
Like in the previous stage, print the information about the number of found errors in total and in each field.
The output should have the same formatting as shown in the example.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the time format is military time (24 hours, hh:mm), which does not mean that all the digits are present. Keep in mind certain restrictions: for example, the first digit cannot be 3, 4, and so on.

Example
Input:

[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Av.",
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
        "a_time": "8:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "OO",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:77"
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
        "stop_name": "Elm",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "A",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10.12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "bourbon street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "38:13"
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

Format validation: 9 errors
stop_name: 3
stop_type: 2
a_time: 4'''

import json
import re


def stage_2(json_final):
    stop_name, stop_type, a_time = 0, 0, 0
    for x in json_final:
        if not re.match(r'^[A-Z].* Street$|^[A-Z].* Avenue$|^[A-Z].* Boulevard$|^[A-Z].* Road$', x["stop_name"]):
            #print(x["stop_name"])
            stop_name += 1
        if len(x["stop_type"]) != 0 and not re.match(r'^[SOF]$', x["stop_type"]):
            stop_type += 1
        if not re.match(r'^[0-2][0-9]:[0-5][0-9]$', x["a_time"]):
            a_time += 1
    print(f"Format validation: {stop_name + stop_type + a_time} errors")
    print(f"stop_name: {stop_name}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")


easy_rider = json.loads(input())
stage_2(easy_rider)

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


def process():
    # json_string = json.dumps(json_data)
    json_string = input()
    prepare(json.loads(json_string))
    prepare_errors()


def prepare(data: list):
    for row in data:
        prepare_row(row)


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


process()

\\
import re
some_string = json.loads(input())


a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in some_string:


    if re.match(r'[A-Z].+\s(Avenue|Street|Road|Boulevard)$', i["stop_name"]) is None:
        c += 1
        print(i['stop_name'])
    if re.match(r'[SOF]$|(^$)', i["stop_type"]) is None:
        e += 1
    if re.match(r'([0-1][0-9]:[0-5][0-9])$|([2][0-3]:[0-5][5-9])$', i["a_time"]) is None:
        f += 1


            
print(f"Format validation: {c+e+f} errors")

print(f"stop_name: {c}")
print(f"stop_type: {e}")
print(f"a_time: {f}")


