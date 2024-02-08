student_scores = {
    "ruby": [85, 90, 92],
    "james": [78, 80, 85],
    "jam": [69, 75, 80] #top G

}


#ruby_grades = student_scores['ruby']

#print(ruby_grades)

#for grades in alice_grades:
    #print(grade)

student_grades = [student_scores ['ruby'],
student_scores['james'],
student_scores['jam']
]


for student, grades in student_scores.items(): 
    print(student)
    for grade in grades:
        print(grade)


