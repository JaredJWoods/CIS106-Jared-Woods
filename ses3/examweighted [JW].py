exam1 = float(input())
exam2 = float(input())
exam1w = float(exam1 * 0.6)
exam2w = float(exam2 * 0.4)
grade = int(exam1w + exam2w)

print("Exam1 counts for 60% of your grade. You scored: ", exam1, "%.")
print("Exam2 counts for 40% of your grade. You scored: ", exam2, "%.")
print("Your final grade is: ", grade, "%.")
