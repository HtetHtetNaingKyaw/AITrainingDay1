GRADE_CATEGORIES = ("Fail", "Pass", "Good", "Excellent")

students = [
    {"name": "Aung Aung", "age": 21, "study_hours": 4.5, "score": 85},
    {"name": "Su Su", "age": 20, "study_hours": 3.0, "score": 65},
    {"name": "Mg Mg", "age": 19, "study_hours": 2.0, "score": 35},
    {"name": "Mya Mya", "age": 22, "study_hours": 5.0, "score": 92},
    {"name": "Kyaw Kyaw", "age": 21, "study_hours": 1.5, "score": 50}
]

def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return GRADE_CATEGORIES[3]  
    elif score >= 60:
        return GRADE_CATEGORIES[2] 
    elif score >= 40:
        return GRADE_CATEGORIES[1] 
    else:
        return GRADE_CATEGORIES[0]  

def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def count_passed(students_list):
    passed_count = 0
    for student in students_list:
        if student["score"] >= 40:
            passed_count += 1
    return passed_count

def display_performance_report(students_list):
    print("===== STUDENT PERFORMANCE REPORT =====")
    
    for student in students_list:
        grade = classify_grade(student["score"])
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Study Hours: {student['study_hours']}")
        print(f"Score: {student['score']}")
        print(f"Grade: {grade}")
        print() 

    scores = [student["score"] for student in students_list]
    
    total_students = len(students_list)
    avg_score = calculate_average(scores)
    highest_score = max(scores) if scores else 0
    lowest_score = min(scores) if scores else 0
    passed_students = count_passed(students_list)
    failed_students = total_students - passed_students
    
    top_students = [s["name"] for s in students_list if s["score"] == highest_score]
    top_student_str = ", ".join(top_students)

    print("===== SUMMARY =====")
    print(f"Total Students: {total_students}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")
    print(f"Top Student: {top_student_str}")

display_performance_report(students)