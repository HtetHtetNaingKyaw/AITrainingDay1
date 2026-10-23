mark = float(input("Enter your mark: "))

if mark <0 or mark >100:
    print("Invalid marks")
elif mark >=80:
    print("Excellent")
elif mark >= 60:
    print("Good")
elif mark >= 40:
    print("Pass")
else:
    print("Fail")

