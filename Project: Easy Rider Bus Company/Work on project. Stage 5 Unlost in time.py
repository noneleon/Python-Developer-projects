'''
Description
It is now time to move on to a more detailed analysis. First, check that arrival times for the upcoming stops make sense: they are supposed to be increasing, that is, going forward in time. After all, there is no information in the documentation that your company offers time travel.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Check that the arrival time for the upcoming stops for a given bus line is increasing.
If the arrival time for the next stop is earlier than or equal to the time of the current stop, stop checking that bus line and remember the name of the incorrect stop.
Display the information for those bus lines that have time anomalies. For the correct stops, do not display anything.
If all the lines are correct timewise, print OK.
The output should have the same formatting as shown in the example.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

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
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:17"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:07"
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
        "a_time": "09:44"
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

Arrival time test:
bus_id line 128: wrong time on station Fifth Avenue
bus_id line 256: wrong time on station Sunset Boulevard
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

Arrival time test:
OK
 Report a typo
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


def stage_5(json_final):
    print("Arrival time test:")
    error = 0
    stops_all = stops(json_final)
    for x in stops_all:
        times, start = {}, ""
        for y in stops_all[x]:
            if y["stop_type"] == "S":
                start = str(y["stop_id"])
            times[str(y["stop_id"])] = (str(y["next_stop"]), y["a_time"], y["stop_name"])
        e, t, n = times[start]
        while e != "0":
            if t >= times[e][1]:
                print(f"bus_id line {x}: wrong time on station {times[e][2]}")
                error += 1
                break
            e, t, n = times[e]
    if error == 0:
        print("OK")


easy_rider = json.loads(input())
stage_5(easy_rider)

\\
import json
from collections import defaultdict

counter_time = 0
counter = 0
list_start = []
list_stop = []
nb_start = 0
nb_stop = 0



some_string = json.loads(input())
bus_list = []
stop_list = []
name_list = []
transfer_list = []
time_list = []
time_list_integer = []

for i in some_string:
    time_list.append((i["a_time"]))

for i in time_list:
    new_string = int(i.replace(":",""))
    time_list_integer.append(new_string)




for i in some_string:
    bus_list.append(i["bus_id"])

for i in some_string:
    name_list.append(i["stop_name"])

for i in some_string:
    stop_list.append(i["stop_type"])


zip_stop = list(zip(bus_list, stop_list))
zip_names = list(zip(bus_list, name_list))
zip_time = list(zip(bus_list, time_list))


d = defaultdict(list)
for a, b in zip_stop:
    d[a].append(b)
sorted(d.items())


dict_name = defaultdict(list)
for a, b in zip_names:
    dict_name[a].append(b)
sorted(dict_name.items())


dict_time = defaultdict(list)
for a, b, in zip_time:
    dict_time[a].append(b)
sorted(dict_time.items())













print("Arrival time test:")
for i in dict_time:
    for a in range(len(dict_time[i])-1):
        if int(dict_time[i][a+1].replace(":", "")) - int(dict_time[i][a].replace(":", "")) <= 0:
            print(f"bus_id line {i}: wrong time on station {dict_name[i][a+1]}")
            counter += 1
            break

if counter ==0:
    print("OK")

    
\\
# Write your awesome code here
import json

data = json.loads(input())


def decimal(t):
    str_vals = t.split(":")
    return float(str_vals[0]) + float(str_vals[1])/60


def positive_timediff(t1, t2):
    return decimal(t2) > decimal(t1)


time_info = dict()

for station in data:
    bus_id = station["bus_id"]
    if not time_info.get(bus_id, False):
        time_info[bus_id] = {}
    time_info[bus_id][station['stop_id']] = {
        "name": station['stop_name'],
        "time": station['a_time'],
        'next_stop': station['next_stop']}

print("Arrival time tests:")
ok = True
for bus_id, bus_info in time_info.items():
    for id, values in bus_info.items():
        next_stop = values['next_stop']
        if next_stop in bus_info:
            if not positive_timediff(values['time'], bus_info[next_stop]['time']):
                print(f"bus_id line {bus_id}: wrong time on station {bus_info[next_stop]['name']}")
                ok = False
                break

if ok:
    print("OK")


