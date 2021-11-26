'''
Description
It seems like our potential students are upset because of the last change in our algorithm. Instead of passing one exam, many of them need to worry about passing two exams with good scores. We are ready to give them a second chance. Now they can try to pass a special university admission exam! If the candidate's score on this exam is better than their mean score for the finals required by a Department, the university is ready to discard the results of the finals.

Objectives
At this stage, your program should:

Read an N integer from the input. This integer represents the maximum number of students for each department.
Read the file named applicants.txt once again. Mind one additional column, right after the last exam's result. This column represents the special exam's score. For example, Willie McBride 76 45 79 80 100 Physics Engineering Mathematics(where 100 is the admission exam's score).
Choose the best score for a student in the ranking: either the mean score for the final exam(s) or the special exam's score. Use the same set of finals for each Department as in the previous stage. Note that you may need to compare the values several times: for example, if a student doesn't get accepted to the Department of the first priority, compare the finals mean score and the special exam's score once again (but this time, for the second priority department).
Keep the rest of the steps the same as in the previous stage. Once again, there should be no more than N accepted applicants for each department; use the same principles for sorting.
Output the names and the student's best score, either the mean finals score or the special exam's score to the files.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Below is an extract of the input file:

Natha Keefe 71 67 53 60 31 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 80 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 59 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 40 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 38 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 59 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 44 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 72 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 50 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 30 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 22 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 78 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 41 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 80 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 75 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 80 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 36 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 79 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 81 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 21 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 69 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 70 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 94 Physics Biotech Engineering
The terminal output:

> 7
The examples of the output to different files:

biotech.txt:

Narissa Worthington 81.0
Randon Bradhust 80.0
chemistry.txt:

Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
engineering.txt:

Lorry Bunger 90.5
Nicolasa Sumpter 88.5
Cheyla Hankinson 87.0
Tommi Peerless 86.5
Cynthia Hermitton 80.0
Marti Mclaws 60.5
Natha Keefe 56.5
mathematics.txt:

Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0
Dashawn Bosley 82.0
physics.txt:

Darrah Smyth 94.0
Cressie Gillespie 83.5
Giovanna Keel 80.0
Fatemah Desavigny 78.0

'''

import os
os.getcwd()

max_nr = int(input())

dep_dict = {'Biotech': [3, 2], 'Chemistry': [3], 'Engineering': [5, 4], 'Mathematics': [4], 'Physics': [2, 4]}
list_appl_1 = []
list_appl_2 = []
list_appl_3 = []

file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_7.txt', 'r')
for i in file:
    list_appl_1.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_7.txt', 'r')
for i in file:
    list_appl_2.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_7.txt', 'r')
for i in file:
    list_appl_3.append(i.replace('\n', '').split())
dep_list_2 = []
for dep in dep_dict.keys():
    lista = []
    dep_lista = []
    for i in range(len(list_appl_1)):
        if list_appl_1[i][7] == dep:
            if len(dep_dict[dep]) == 2:
                mean = (float(list_appl_1[i][dep_dict[dep][0]]) + float(list_appl_1[i][dep_dict[dep][1]])) / 2
            elif len(dep_dict[dep]) == 1:
                mean = float(list_appl_1[i][dep_dict[dep][0]])
            best = max(mean, float(list_appl_1[i][6]))
            list_appl_1[i].append(best)
            lista.append(list_appl_1[i])
    lista = sorted(lista, key=lambda x: (-float(x[10]), x[0], x[1]))
    for i in range(len(lista)):
        if i < max_nr:
            dep_lista.append([lista[i][0], lista[i][1], lista[i][10]])
            lista[i].remove(lista[i][10])
            list_appl_2.remove(lista[i])
            list_appl_3.remove(lista[i])
    dep_list_2.append(dep_lista)
for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_2)):
        if list_appl_2[i][8] == list(dep_dict.keys())[n]:
            if len(dep_dict[list(dep_dict.keys())[n]]) == 2:
                mean = (float(list_appl_2[i][dep_dict[list(dep_dict.keys())[n]][0]]) + float(
                    list_appl_2[i][dep_dict[list(dep_dict.keys())[n]][1]])) / 2
            elif len(dep_dict[list(dep_dict.keys())[n]]) == 1:
                mean = float(list_appl_2[i][dep_dict[list(dep_dict.keys())[n]][0]])
            best = max(mean, float(list_appl_2[i][6]))
            list_appl_2[i].append(best)
            lista.append(list_appl_2[i])
    lista = sorted(lista, key=lambda x: (-float(x[10]), x[0], x[1]))

    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - nr:
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][10]])
                lista[i].remove(lista[i][10])
                list_appl_3.remove(lista[i])
for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_3)):
        if list_appl_3[i][9] == list(dep_dict.keys())[n]:
            if len(dep_dict[list(dep_dict.keys())[n]]) == 2:
                mean = (float(list_appl_3[i][dep_dict[list(dep_dict.keys())[n]][0]]) + float(
                    list_appl_3[i][dep_dict[list(dep_dict.keys())[n]][1]])) / 2
            elif len(dep_dict[list(dep_dict.keys())[n]]) == 1:
                mean = float(list_appl_3[i][dep_dict[list(dep_dict.keys())[n]][0]])
            best = max(mean, float(list_appl_3[i][6]))
            list_appl_3[i].append(best)
            lista.append(list_appl_3[i])
    lista = sorted(lista, key=lambda x: (-float(x[10]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - len(dep_list_2[n]):
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][10]])
dep_list_3 = []
for n in range(len(dep_dict)):
    lista = sorted(dep_list_2[n], key=lambda x: (-float(x[2]), x[0], x[1]))
    dep_list_3.append(lista)

for n in range(len(dep_dict)):
    dep_name = list(dep_dict.keys())[n]
    file = open(f'{dep_name}.txt', 'w', encoding='utf-8')
    for i in dep_list_3[n]:
        file.write(f'{i[0]} {i[1]} {i[2]}\n')
    file.close()
    
    
\\




