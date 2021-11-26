'''
Description
You just started sorting out the existing database of the "Easy Rider" bus company. As you take the first look at the data, you realize that it's not going to be easy.

Sometimes numbers are missing from where they should definitely be. You also noticed that sometimes there are too many or too few characters. Fortunately, there is documentation to help you sort out this mess. However, this documentation is not a hundred percent complete: part of it was torn away when your colleague spilled coffee on it. Let's see what we can make out.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Check that the data types match.
Check that the required fields are filled in.
Display the information about the number of found errors in total and in each field.
The output should have the same formatting as shown in the example.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the type Char is present among the data types.

Example
Input:

[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
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
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
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
        "next_stop": "0",
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
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]
Output:

Type and required field validation: 8 errors
bus_id: 2
stop_id: 1
stop_name: 1
next_stop: 1
stop_type: 1
a_time: 2
 Report a typo
'''

import json


def stage_1(json_final):
    bus_id, stop_id, stop_name, next_stop, stop_type, a_time = 0, 0, 0, 0, 0, 0
    for x in json_final:
        if not isinstance(x["bus_id"], int):
            bus_id += 1
        if not isinstance(x["stop_id"], int):
            stop_id += 1
        if not isinstance(x["stop_name"], str) or x["stop_name"] == "":
            stop_name += 1
        if not isinstance(x["next_stop"], int) or x["next_stop"] == "":
            next_stop += 1
        if not isinstance(x["stop_type"], str) or len(x["stop_type"]) > 1:
            stop_type += 1
        if not isinstance(x["a_time"], str) or x["a_time"] == "":
            a_time += 1
    print(f"{bus_id + stop_id + stop_name + next_stop + stop_type + a_time} errors")
    print(f"bus_id: {bus_id}")
    print(f"stop_id: {stop_id}")
    print(f"stop_name: {stop_name}")
    print(f"next_stop: {next_stop}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")

easy_rider = json.loads(input())
stage_1(easy_rider)


\\
# Write your awesome code here
import json
import re
from collections import Counter


class BusChecker:
    def __init__(self, easy_rider_data: list, field_requirements=None):
        self.field_requirements = field_requirements or {
            "bus_id": {"type": int, "required": True, "format": self.is_positive},
            "stop_id": {"type": int, "required": True, "format": self.is_positive},
            "stop_name": {"type": str, "required": True, "format": self.is_stop_name},
            "next_stop": {"type": int, "required": True, "format": self.is_positive},
            "stop_type": {"type": str, "required": False, "format": self.is_stop_type},
            "a_time": {"type": str, "required": True, "format": self.is_time_format},
        }
        self.easy_rider_data = easy_rider_data
        self.error_counter = Counter()

    def print_errors(self):
        self.easy_rider_check()
        print(f"Type and required field validation: {sum(self.error_counter.values())} errors")
        order = ["bus_id", "stop_id", "stop_name", "next_stop", "stop_type", "a_time"]
        for field in order:
            print(f"{field}: {self.error_counter[field]}")

    def easy_rider_check(self):
        for row in self.easy_rider_data:
            self.row_check(row)
        return self.error_counter

    def row_check(self, row):
        for field in self.field_requirements:

            if not isinstance(row[field], self.field_requirements[field]["type"]):
                self.error_counter[field] += 1

                continue
            elif not self.field_requirements[field]["format"](row[field]):
                self.error_counter[field] += 1
                if field == "stop_type":
                    print(field, row[field])
                continue
            elif self.field_requirements[field]['required'] and row[field] is None:
                self.error_counter[field] += 1

                continue

    def is_stop_name(self, value):
        return type(value) == str and bool(value)

    def is_stop_type(self, stop):
        return stop in ("S", "O", "F") or stop == ""

    def is_positive(self, value: int) -> bool:
        return value >= 0

    def is_time_format(self, s: str) -> bool:
        time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
        return bool(time_re.match(s))


def main():
    # with open("test.json", encoding="utf-8") as file:
    #     buses = json.load(file)
    buses = json.loads(input())
    bus_checker = BusChecker(easy_rider_data=buses)
    bus_checker.print_errors()


if __name__ == '__main__':
    main()

