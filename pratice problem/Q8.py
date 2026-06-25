# Question 8: Employee Bonus Calculator 
# Question: Create a function calculate_bonus(salary, experience) that calculates an employee's bonus based on the following
#  conditions: 
# ● Experience ≥ 10 years → 20% of salary 
# ● Experience ≥ 5 years and < 10 years → 10% of salary 
# ● Experience < 5 years → 5% of salary 
# Print the bonus amount. 
# Input: 
# 50000 
# 7 
# Output: 
# 5000.0
def calculate_bonus(salary, experience):
    if experience >=10:
        bonus = salary * 0.20
    elif experience >=5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    
    return bonus

salary = int (input("Enter the Value:"))
experience = int (input("Enter the Value:"))

result = calculate_bonus(salary, experience)
print(int(result))