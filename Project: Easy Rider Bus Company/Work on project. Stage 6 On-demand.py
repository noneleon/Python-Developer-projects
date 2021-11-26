'''
Description
The work seemed tedious and endless, but it finally looks like we're getting there. There is only one more point left in the specification that we need to check and fix: on-demand stops cannot be initial, final, or transfer stops.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Check that all the departure points, final stops, and transfer stations are not "On-demand".
Display the unique names of the stops containing this type of issue. Sort them in ascending order.
If everything is fine, print OK.
The output should have the same formatting as shown in the example.
If you cannot find the necessary information in the stage description, it can probably be found in the attached documentation.

Examples
Example 1

Input 1:

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
        "stop_type": "O",
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
        "stop_type": "O",
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
Output 1:

On demand stops test:
Wrong stop type: ['Elm Street', 'Sunset Boulevard']
Example 2

Input 2:

[
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
Output 2:

On demand stops test:
OK
 Report a typo

'''

import json

def stage_6(json_final):
    print("On demand stops test:")
    all_stops = {}
    for z in set([x["bus_id"] for x in json_final]):
        all_stops[z] = [x for x in json_final if x["bus_id"] == z]
    station_all = [x["stop_name"] for y in all_stops for x in all_stops[y]]
    station_sf = [x["stop_name"] for y in all_stops for x in all_stops[y] if x["stop_type"] in ("SF") and x["stop_type"] != ""]
    station_o = [x["stop_name"] for y in all_stops for x in all_stops[y] if x["stop_type"] in ("O") and x["stop_type"] != ""]
    station_t = sorted([x for x in set(station_all) if station_all.count(x) > 1])
    stations = (set(station_sf) | set(station_t)) & set(station_o)
    if stations:
        print(f"Wrong stop type: {sorted(stations)}")
    else:
        print("OK")


easy_rider = json.loads(input())
stage_6(easy_rider)

\\

import json

bus_data = json.loads(input())
departure_stops, final_stops, transfer_stops, stops_with_already_one_line, on_demand_stops = set(), set(), set(), set(), set()


def stop_categorizer(stop_type, name):
    if stop_type == 'S':
        departure_stops.add(name)
    elif stop_type == 'F':
        final_stops.add(name)
    transfer_stop_detector(name)
    on_demand_stop_check(stop_type, name)


def transfer_stop_detector(name):
    if name in stops_with_already_one_line:
        transfer_stops.add(name)


def on_demand_stop_check(stop_type, name):
    if stop_type == 'O':
        on_demand_stops.add(name)


def error_with_on_demand_stops_check():
    not_valid_on_demand_stops = departure_stops | final_stops | transfer_stops
    print('On demand stops test:')
    wrong_stops = not_valid_on_demand_stops.intersection(on_demand_stops)
    if wrong_stops:
        print(f'Wrong stop type: {sorted(wrong_stops)}')
    else:
        print('OK')


def data_processing(bus):
    stop_categorizer(bus['stop_type'], bus['stop_name'])
    stops_with_already_one_line.add(bus['stop_name'])


def main():
    for instance in bus_data:
        data_processing(instance)
    error_with_on_demand_stops_check()
    

if __name__ == '__main__':
    main()
    
\\

from collections import defaultdict
import json


data_dict = json.loads(input())
transfer_stops = set()
stops = set()
wrong_stops = []

for j in data_dict:
    if j["stop_name"] in stops:
        transfer_stops.add(j["stop_name"])
    stops.add(j["stop_name"])

for j in data_dict:
    if j["stop_name"] in transfer_stops:
        if j["stop_type"] == "O":
            wrong_stops.append(j["stop_name"])

print("On demand stops test:")
if len(wrong_stops) == 0:
    print("OK")
else:
    print("Wrong stop type: {}".format(sorted(wrong_stops)))