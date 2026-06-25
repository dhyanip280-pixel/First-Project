# Question 9: Student Result Analyzer 
# Question: Create a function calculate_result(mark1, mark2, mark3) that returns: 
# ● "Distinction" if average ≥ 75 
# ● "First Class" if average ≥ 60 and < 75 
# ● "Second Class" if average ≥ 40 and < 60 
# ● "Fail" if average < 40 
# Use exception handling to ensure all marks are between 0 and 100. If any mark is invalid, print 
# "Invalid Marks". 
# Input: 
# 85 
# 78 
# 90 
# Output: 
# Distinction
# Input: 
# 95 
# 120 
# 80 
# Output: 
# Invalid Marks 

def calculate_result(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3

    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Class"
    elif average >= 40:
        return "Second Class"
    else:
        return "Fail"


mark1 = int(input("Enter the Value :"))
mark2 = int(input("Enter the Value :"))
mark3 = int(input("Enter the Value :"))

result = calculate_result(mark1, mark2, mark3)

print("Answer :",result)