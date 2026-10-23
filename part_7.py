# def greet():
#     print("Welcome to Python for AI!")

# greet()

# def greet_user(name):
#     print (f"Hello, {name}")

# greet_user("John Smith")
# greet_user("Ko Ko")

# def calculate_average(scores):
#     if (len(scores) == 0):
#         return 0
#     return sum(scores) /len(scores)

# scores = [45,70,85,]
# result = calculate_average(scores)
# print(f"The average score is: {result}")

def calculate_total(scores):
    return sum(scores)

def calculate_average(scores):
   if (len(scores) == 0):
        return 0
   return sum(scores) / len(scores)

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
    for score in scores:
        if score >=40:
            passed_scores += 1
    return passed_scores

scores = [45, 70, 85, 30, 90, 55]

result_total = calculate_total(scores)
result_grade = classify_grade(90)
result_average = calculate_average(scores)
result_passed = count_passed(scores)

print(f"Total: {result_total}")
print(f"Average: {result_average}")
print(f"Grade: {result_grade}")
print(f"Passed Count: {result_passed}")
