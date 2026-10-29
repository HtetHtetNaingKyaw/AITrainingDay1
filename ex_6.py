students = [
{"name": "Aung Aung", "score": 85},
{"name": "Su Su", "score": 92},
{"name": "Mg Mg", "score": 35}
]

def classify_grade(scores):
    if scores < 0 or scores > 100:
        return "Invalid"
    elif scores >= 80:
        return "Excellent"
    elif scores >= 60:
        return "Good"
    elif scores >= 40:
        return "Pass"
    else:
        return "Fail"

def count_passed(scores):
    passed_scores = 0
    if scores >=40:
        passed_scores += 1
        return passed_scores


for student in students:

    if(count_passed(student['score'])):
        print(f"Passing Studnet : {student['name']} passed with {student['score']}")
    
    print(f"Student name : {student['name']} {student['score']}")
    print(f"Grade Score : {classify_grade(student['score'])}")

new_student = {"name":"Mya Mya","score":40}
students.append(new_student)

print(students)