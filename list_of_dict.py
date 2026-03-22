students=[
    {'Name':'Ali','House':'Iqbal','Class':'12'},
    {'Name':'Amir','House':'Jinnah','Class':'12'},
    {'Name':'Ali','House':'Iqbal','Class':'None'},
]
for student in students:
    print(student['Name'],student['House'],student['Class'],sep=', ')
