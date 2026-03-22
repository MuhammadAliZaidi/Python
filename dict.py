students={
    "Ali":"Iqbal",
     "Ahmad":"Jinnah",
     "Amir":"Jinnah",
}
print(students['Ali'])
print(students['Ahmad'])
print(students["Amir"])
for student in students:
    print(student,students[student],sep=', ')
