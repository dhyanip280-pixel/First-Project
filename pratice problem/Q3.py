# Question 3: Grade Calculator 
# Question: Write a program that takes a student's marks and prints the grade using the following conditions:
# ● 90 and above → A 
# ● 75 to 89 → B 
# ● 50 to 74 → C 
# ● Below 50 → Fail 
# Input: 
# 82 
# Output: 
# B 

marks = float(input("Enter the student's marks: "))

if marks >= 90:
    print("Grade = A")
elif marks >= 75:
    print("Grade = B")
elif marks >= 50:
    print("Grade = C")
else:
    print("Grade = F")