'''
Description
Taking only student's GPAs into consideration may not be very conclusive. It would be better if we could take the results of the finals depending on the Department. For example, for a Physics department candidate, we would check the physics finals. Try to take the sorting algorithm to the next level. In this stage, you need to sort by an exam that suits the particular Department.

Objectives
At this stage, your program should:

Read an N integer. This integer represents the maximum number of students for each department.
Read the file named applicants.txt once again. The structure has changed a bit: instead of the GPA column, each line contains four columns with scores for particular exams: physics, chemistry, math, computer science (in this order). For example, John Ritchie 89 45 83 75 Physics Engineering Mathematics.
Take into account the following exam results for the departments: physics for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science for the Engineering, and chemistry (again) for the Biotech department.
Do the same steps as in the previous stage: perform three stages of admission based on the applicants' priorities. Applicants should be ranked by their exam score and, in case they have the same score, their full name in alphabetic order. There should be no more than N accepted applicants for each department. One student can only be accepted to one department.
One thing has changed — output the exam result (instead of the GPA) for each student:
department_name
applicant1 exam1
applicant2 exam2
applicant3 exam3
<...>
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Below is an example of the input file:

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
This is an example of the output:

> 5
Biotech
Randon Bradhust 88.0
Marti Mclaws 71.0
Narissa Worthington 71.0
Natha Keefe 67.0

Chemistry
Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
Dashawn Bosley 79.0

Engineering
Lorry Bunger 97.0
Tommi Peerless 92.0
Cheyla Hankinson 88.0
Cynthia Hermitton 88.0
Nicolasa Sumpter 81.0

Mathematics
Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0

Physics
Cressie Gillespie 85.0
Giovanna Keel 84.0
Fatemah Desavigny 81.0
Darrah Smyth 75.0

'''
import os
os.getcwd()

max_nr = int(input())

dep_dict = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}
list_appl_1 = []
list_appl_2 = []
list_appl_3 = []

file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_5.txt', 'r')
for i in file:
    list_appl_1.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_5.txt', 'r')
for i in file:
    list_appl_2.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_5.txt', 'r')
for i in file:
    list_appl_3.append(i.replace('\n', '').split())

dep_list_2 = []
for dep in dep_dict.keys():
    lista = []
    dep_lista = []
    for i in range(len(list_appl_1)):
        if list_appl_1[i][6] == dep:
            lista.append(list_appl_1[i])
    lista = sorted(lista, key=lambda x: (-float(x[dep_dict[dep]]), x[0], x[1]))
    for i in range(len(lista)):
        if i < max_nr:
            dep_lista.append([lista[i][0], lista[i][1], lista[i][dep_dict[dep]]])
            list_appl_2.remove(lista[i])
            list_appl_3.remove(lista[i])
    dep_list_2.append(dep_lista)

for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_2)):
        if list_appl_2[i][7] == list(dep_dict.keys())[n]:
            lista.append(list_appl_2[i])
    lista = sorted(lista, key=lambda x: (-float(x[dep_dict[list(dep_dict.keys())[n]]]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - nr:
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][dep_dict[list(dep_dict.keys())[n]]]])
                list_appl_3.remove(lista[i])

for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_3)):
        if list_appl_3[i][8] == list(dep_dict.keys())[n]:
            lista.append(list_appl_3[i])
    lista = sorted(lista, key=lambda x: (-float(x[dep_dict[list(dep_dict.keys())[n]]]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - len(dep_list_2[n]):
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][dep_dict[list(dep_dict.keys())[n]]]])

dep_list_3 = []
for n in range(len(dep_dict)):
    lista = sorted(dep_list_2[n], key=lambda x: (-float(x[2]), x[0], x[1]))
    dep_list_3.append(lista)

for n in range(len(dep_dict)):
    print(list(dep_dict.keys())[n])
    for i in dep_list_3[n]:
        print(f'{i[0]} {i[1]} {i[2]}')
    print('')
    
\\
def read_entrants(file_name):
    file = open(file_name, 'r')
    students = []
    for line in file:
        s = line.strip('\n').split()
        students.append({'name': s[0],
                         'last name': s[1],
                         'exams': {'physics': float(s[2]), 'chemistry': float(s[3]), 'math': float(s[4]),
                                   'computer science': float(s[5])},
                         'departments': s[6:]})
    return students


def get_departments():
    return {'Biotech': {'applicants': [], 'exam': 'chemistry'},
            'Chemistry': {'applicants': [], 'exam': 'chemistry'},
            'Engineering': {'applicants': [], 'exam': 'computer science'},
            'Mathematics': {'applicants': [], 'exam': 'math'},
            'Physics': {'applicants': [], 'exam': 'physics'}}


def choose_applicants(applicant_quota, applicants):
    university = get_departments()

    for i in range(3):
        departments_candidates = get_departments()
        # sort applicants by preferred department
        for applicant in applicants:
            chooses_dep = departments_candidates[applicant['departments'][i]]
            chooses_dep['applicants'].append(applicant)
        # Allocate applicants to departments
        for department_name, attributes in departments_candidates.items():
            dep_candidates = department_name
            exam = attributes['exam']
            candidates = attributes['applicants']
            selection_bias = lambda s: (-s['exams'][exam], s['name'], s['last name'])
            candidates.sort(key=selection_bias)
            department = university[dep_candidates]['applicants']
            if len(department) < applicant_quota:
                if len(candidates) > applicant_quota - len(department):
                    department.extend(candidates[: applicant_quota - len(department)])
                else:
                    department.extend(candidates)
            department.sort(key=selection_bias)
            # remove entered applicants
            for entered_applicant in department:
                if entered_applicant in applicants:
                    applicants.remove(entered_applicant)

        departments_candidates.clear()
    return university


def print_applicants(applicants):
    for department_name, department in applicants.items():
        print(department_name)
        exam = department['exam']
        entered = department['applicants']
        for person in entered:
            print(f"{person['name']} {person['last name']} {person['exams'][exam]}")
        print()


def go():
    applicant_quota = int(input())
    applicants = read_entrants('./applicant_list_5.txt')
    entered_applicants = choose_applicants(applicant_quota, applicants)
    print_applicants(entered_applicants)


go()


