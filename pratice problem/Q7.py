# Question 7: Function with Multiple Parameters 
# Question: Create a function calculate_salary(basic, hra, bonus) that returns the total salary. Take the three values as input 
# and print the result. 
# Input: 
# 25000 
# 5000 
# 2000 
 
# Output: 
# 32000
def calculate_salary(basic, hra, bonus) :
    Salary = basic + hra + bonus
    return Salary
basic = int (input("Enter the Value:"))
hra = int (input("Enter the Value:"))
bonus = int (input("Enter the Value:"))

result = calculate_salary(basic, hra, bonus)

print("Answer:",result)