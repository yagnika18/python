stud_marks={
    'huk':87,
    'uik':90,
    'qazh':12,
    'idw':46,
    'ijdk':73
}
stude_grades={}
for student in stud_marks:
    marks=stud_marks[student]
    if marks>90:
        stude_grades[student]="A+"
    elif marks>80:
        stude_grades[student]="A"
    elif marks>70:
        stude_grades[student]="B"
    elif marks>60:
        stude_grades[student]="c"
    elif marks>50:
        stude_grades[student]="D"
    elif marks>40:
        stude_grades[student]="E"
    else:
        stude_grades[student]="F"
print(stude_grades)