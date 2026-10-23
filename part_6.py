# # for i in range(5):
# #     print(i)

# # scores = [75, 85, 90, 60, 45]
# # for score in scores:
# #     print(score)

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

scores = [45, 70, 85, 30, 90, 55]

failing_scores = 0
passing_scores = 0
total = 0
for score in scores:
    total += score

average = total / len(scores)

print("Total:", total)
print("Average:", average)

for i in scores:
    if i < 40:
        failing_scores += 1
    else:
        passing_scores += 1

print("Failing Scores:", failing_scores)
print("Passing Scores:", passing_scores)
