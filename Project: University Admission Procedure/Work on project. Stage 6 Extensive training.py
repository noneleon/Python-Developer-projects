'''
Description
Some of the departments proposed an improvement to the algorithm. They need more than one exam results for each applicant. For example, the Physics Department needs both math and physics exams, while the Mathematics Department is satisfied with the math exam only. Let's implement this request to make our departments happy (the applicants on the other hand...)

Objectives
At this stage, your program should:

Read an N integer from the input. This integer represents the maximum number of students for each department.
Read the file named applicants.txt once again. The file has the same structure as in the previous stage.
Consider the following exam results for departments: physics and math for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department.
As in the previous stage, the exams are listed in the following order for each applicant: physics, chemistry, math, computer science.
For the departments that need several exams, calculate the mean score and use it to rank the applicants (use floating-point numbers with at least one decimal). Otherwise, use the result for a single exam.
Keep the rest of the steps the same as in the previous stage (once again, there should be no more than N accepted applicants for each department; use the same principles for sorting).
Instead of printing the results (you may do it if you want), output the admission lists to files. Create a file for each department, name it %department_name%.txt, for example, physics.txt. Write the names of the students accepted to the department and their mean finals score to the corresponding file (one student per line).
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Below is an extract of the input file:

Natha Keefe 71 67 53 60 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 Physics Biotech Engineering
The terminal output:

> 7
The examples of the output to different files:

biotech.txt:

Randon Bradhust 80.0
Narissa Worthington 61.5
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
Cynthia Hermitton 75.0
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

Cressie Gillespie 83.5
Giovanna Keel 80.0
Darrah Smyth 79.5
Fatemah Desavigny 77.0

'''
import os
os.getcwd()

max_nr = int(input())

dep_dict = {'Biotech': [3, 2], 'Chemistry': [3], 'Engineering': [5, 4], 'Mathematics': [4], 'Physics': [2, 4]}
list_appl_1 = []
list_appl_2 = []
list_appl_3 = []

file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_6.txt', 'r')
for i in file:
    list_appl_1.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_6.txt', 'r')
for i in file:
    list_appl_2.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_6.txt', 'r')
for i in file:
    list_appl_3.append(i.replace('\n', '').split())

dep_list_2 = []
for dep in dep_dict.keys():
    lista = []
    dep_lista = []
    for i in range(len(list_appl_1)):
        if list_appl_1[i][6] == dep:
            if len(dep_dict[dep]) == 2:
                mean = (float(list_appl_1[i][dep_dict[dep][0]]) + float(list_appl_1[i][dep_dict[dep][1]])) / 2
            elif len(dep_dict[dep]) == 1:
                mean = float(list_appl_1[i][dep_dict[dep][0]])
            list_appl_1[i].append(mean)
            lista.append(list_appl_1[i])
    lista = sorted(lista, key=lambda x: (-float(x[9]), x[0], x[1]))
    for i in range(len(lista)):
        if i < max_nr:
            dep_lista.append([lista[i][0], lista[i][1], lista[i][9]])
            lista[i].remove(lista[i][9])
            list_appl_2.remove(lista[i])
            list_appl_3.remove(lista[i])
    dep_list_2.append(dep_lista)

for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_2)):
        if list_appl_2[i][7] == list(dep_dict.keys())[n]:
            if len(dep_dict[list(dep_dict.keys())[n]]) == 2:
                mean = (float(list_appl_2[i][dep_dict[list(dep_dict.keys())[n]][0]]) + float(
                    list_appl_2[i][dep_dict[list(dep_dict.keys())[n]][1]])) / 2
            elif len(dep_dict[list(dep_dict.keys())[n]]) == 1:
                mean = float(list_appl_2[i][dep_dict[list(dep_dict.keys())[n]][0]])
            list_appl_2[i].append(mean)
            lista.append(list_appl_2[i])
    lista = sorted(lista, key=lambda x: (-float(x[9]), x[0], x[1]))

    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - nr:
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][9]])
                lista[i].remove(lista[i][9])
                list_appl_3.remove(lista[i])

for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_3)):
        if list_appl_3[i][8] == list(dep_dict.keys())[n]:
            if len(dep_dict[list(dep_dict.keys())[n]]) == 2:
                mean = (float(list_appl_3[i][dep_dict[list(dep_dict.keys())[n]][0]]) + float(
                    list_appl_3[i][dep_dict[list(dep_dict.keys())[n]][1]])) / 2
            elif len(dep_dict[list(dep_dict.keys())[n]]) == 1:
                mean = float(list_appl_3[i][dep_dict[list(dep_dict.keys())[n]][0]])
            list_appl_3[i].append(mean)
            lista.append(list_appl_3[i])
    lista = sorted(lista, key=lambda x: (-float(x[9]), x[0], x[1]))

    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - len(dep_list_2[n]):
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][9]])

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

max_students = int(input())

with open('applicants.txt') as applicants_file:
    applicants = [applicant.split() for applicant in applicants_file.readlines()]
codes = ((3, 2), 3, (4, 5), 4, (4, 2))
keys = ('Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics')
departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
departments_list = [[], [], [], [], []]


def department_allocation(applicants_list):
    for i in range(6, 9):
        for applicant in applicants_list:
            departments_list[keys.index(applicant[i])].append(applicant)
        for j in range(5):
            departments_list[j] = sorted(departments_list[j], key=lambda x: (
                -float((float(x[codes[j][0]]) + float(x[codes[j][1]])) / 2 if isinstance(codes[j], tuple) else x[
                    codes[j]]), x[0], x[1]))[: max_students - len(departments[keys[j]])]
            for student in departments_list[j]:
                applicants_list.remove(student)
            departments[keys[j]] += departments_list[j]
            departments[keys[j]].sort(key=lambda x: (
                -float(((float(x[codes[j][0]]) + float(x[codes[j][1]])) / 2) if isinstance(codes[j], tuple) else x[
                    codes[j]]), x[0], x[1]))
            departments_list[j].clear()


department_allocation(applicants)

for key, value in departments.items():
    with open(f'{key.lower()}.txt', 'w', encoding='utf-8') as file:
        for element in value:
            to_write = ' '.join(map(str, [element[0], element[1], float(
                (float(element[codes[keys.index(key)][0]]) + float(
                    element[codes[keys.index(key)][1]])) / 2 if isinstance(
                    codes[keys.index(key)], tuple) else element[codes[keys.index(key)]])]))
            file.write(to_write + '\n')


