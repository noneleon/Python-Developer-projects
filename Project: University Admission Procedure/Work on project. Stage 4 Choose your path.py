'''Description
Good news everyone: our university keeps growing larger! Five departments have been established; now our potential students can apply to the Mathematics, Physics, Biotech, Chemistry, or the Engineering Department. Each applicant needs to choose three departments and rank them. First, the department with the highest priority; second, the department in case the first option doesn't work out. The third department is Plan C.

Your task for this stage is to develop an algorithm that will sort the applicants according to their GPA and take into account their priorities: if the applicant doesn't score high enough to get accepted to the department of first priority, they'll participate in the rankings for the second priority, and so on.

In other words, the admission algorithm should work by the following rules:

Firstly, the ranking list for every department is created according to the applicant's first priorities. People who chose Physics as their first priority only participate in ranking for the Physics department, and so on.
Applicants are scored according to their GPA. People who have a higher GPA score are ranked higher in the department's ranking list.
Each department accepts N (maximum number of students for the department) best students from the department's ranking list. If there are fewer than N students on the department's list, all students from the list are accepted.
The accepted students are removed from the general list of applicants and no longer participate in the ranking.
The same procedure is repeated for the second priorities. If there are departments that accepted fewer than N students in the first stage of admission, these departments try to accept more students to fill all N student positions.
The same procedure is repeated for the third priority.
Hint

The number of applicants is increasing, so instead of parsing the data through the manual input, we've created the file that contains the list of potential students for your program to read. It is much more convenient to provide your program with information on applicants in this way.

Objectives
At this stage, your program should:

Read an N integer from the input. This integer represents the maximum number of students for each department.
Read the file named applicants.txt (this file is already included in the project's files, even though it is not visible; so you only need to download it if you want to take a closer look at it). Each line equals one applicant, their first name, last name, GPA, first priority department, second priority department, and third priority department. Columns with values are separated by whitespace characters. For example, Laura Spungen 3.71 Physics Engineering Mathematics.
Sort applicants according to their GPA and priorities (and names, if their GPA score is the same). As in the previous stage, if two applicants to the same department have the same GPA, sort them by their full names in alphabetical order.
For each department, choose the N best candidates. Some departments are less popular than others, so there may be fewer available candidates for a department. However, their number shouldn't be more than N.
Print the departments in the alphabetic order (Biotech, Chemistry, Engineering, Mathematics, Physics), output the names and the GPA of enrolled applicants for each department. Separate the name and the GPA with a whitespace character. Here's an example (you may add empty lines between the departments' lists to increase the text readability):
department_name
applicant1 GPA1
applicant2 GPA2
applicant3 GPA3
<...>
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1. There are enough students for all departments:

Below is an example of the input file:

Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
An example of the output:

> 4
Biotech
Randon Bradhust 3.68
Narissa Worthington 3.3
Natha Keefe 3.14
Cynthia Hermitton 3.1

Chemistry
Crescentia Dow 3.79
Halima Brydone 3.72
Estephanie Phelps 3.21
Tawny Crockett 3.01

Engineering
Tommi Peerless 3.85
Cheyla Hankinson 3.82
Nicolasa Sumpter 3.82
Lorry Bunger 3.79

Mathematics
Dashawn Bosley 3.54
Aundria Guthrie 3.51
Kennon Inverarity 3.5
Teneil Maclean 3.22

Physics
Darrah Smyth 3.89
Giovanna Keel 3.25
Cressie Gillespie 3.1
Fatemah Desavigny 3.0
Example 2. There aren't enough students for all departments:

The same textfile:

Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
An example of the output:

> 8
Biotech
Randon Bradhust 3.68
Narissa Worthington 3.3

Chemistry
Crescentia Dow 3.79
Halima Brydone 3.72
Estephanie Phelps 3.21
Tawny Crockett 3.01

Engineering
Tommi Peerless 3.85
Cheyla Hankinson 3.82
Nicolasa Sumpter 3.82
Lorry Bunger 3.79
Natha Keefe 3.14
Cynthia Hermitton 3.1
Marti Mclaws 3.05

Mathematics
Dashawn Bosley 3.54
Aundria Guthrie 3.51
Kennon Inverarity 3.5
Teneil Maclean 3.22
Shealynn Melville 3.02
Esther Bratby 2.67

Physics
Darrah Smyth 3.89
Giovanna Keel 3.25
Cressie Gillespie 3.1
Fatemah Desavigny 3.0'''

# write your code here
import os
os.getcwd()

max_nr = int(input())

dep_list = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
list_appl_1 = []
list_appl_2 = []
list_appl_3 = []

file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_4.txt', 'r')
for i in file:
    list_appl_1.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_4.txt', 'r')
for i in file:
    list_appl_2.append(i.replace('\n', '').split())
file = open(r'C:\Users\陆明\PycharmProjects\University Admission Procedure1\University Admission Procedure\task\applicants_4.txt', 'r')
for i in file:
    list_appl_3.append(i.replace('\n', '').split())

dep_list_2 = []
for dep in dep_list:
    lista = []
    dep_lista = []
    for i in range(len(list_appl_1)):
        if list_appl_1[i][3] == dep:
            lista.append(list_appl_1[i])
    lista = sorted(lista, key=lambda x: (-float(x[2]), x[0], x[1]))
    for i in range(len(lista)):
        if i < max_nr:
            dep_lista.append([lista[i][0], lista[i][1], lista[i][2], lista[i][3]])
            list_appl_2.remove(lista[i])
            list_appl_3.remove(lista[i])
    dep_list_2.append(dep_lista)

for n in range(len(dep_list)):
    lista = []
    for i in range(len(list_appl_2)):
        if list_appl_2[i][4] == dep_list[n]:
            lista.append(list_appl_2[i])
    lista = sorted(lista, key=lambda x: (-float(x[2]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - nr:
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][2], lista[i][4]])
                list_appl_3.remove(lista[i])

for n in range(len(dep_list)):
    lista = []
    for i in range(len(list_appl_3)):
        if list_appl_3[i][5] == dep_list[n]:
            lista.append(list_appl_3[i])
    lista = sorted(lista, key=lambda x: (-float(x[2]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - len(dep_list_2[n]):
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][2], lista[i][5]])

dep_list_3 = []
for n in range(len(dep_list)):
    lista = sorted(dep_list_2[n], key=lambda x: (-float(x[2]), x[0], x[1]))
    dep_list_3.append(lista)

for n in range(len(dep_list)):
    print(dep_list[n])
    for i in dep_list_3[n]:
        print(f'{i[0]} {i[1]} {i[2]}')
    print('')
    
    
\\

class Admission:
    def __init__(self, quotes):
        self.quotes = quotes
        self.applications = []
        self.accepted_applications = []
        self.departments = {
            "Biotech": [],
            "Chemistry": [],
            "Engineering": [],
            "Mathematics": [],
            "Physics": []
        }

    def retrieve_data(self):
        with open("applicant_list.txt", 'r') as file:
            for line in file:
                items = line.split()
                application = {
                    "full_name": " ".join(items[:2]),
                    "gpa": float(items[2]),
                    "prior_1": items[3],
                    "prior_2": items[4],
                    "prior_3": items[5]
                }
                self.applications.append(application)

    def make_waves(self):
        for i in range(1, 3 + 1):
            for department in self.departments.keys():
                applications = []

                for application in self.applications:
                    if application[f"prior_{i}"] == department and application not in self.accepted_applications:
                        applications.append(application)

                applications.sort(key=lambda x: (-x["gpa"], x["full_name"]))
                for item in applications[:self.quotes]:
                    if len(self.departments[department]) < self.quotes:
                        self.departments[department].append(item)
                        self.accepted_applications.append(item)

    def students_lists(self):
        for department in self.departments.keys():
            print(department)
            self.departments[department].sort(key=lambda x: (-x["gpa"], x["full_name"]))
            for item in self.departments[department]:
                print(item["full_name"], item["gpa"])
            print()


def main():
    admission = Admission(int(input()))
    admission.retrieve_data()
    admission.make_waves()
    admission.students_lists()


if __name__ == "__main__":
    main()
