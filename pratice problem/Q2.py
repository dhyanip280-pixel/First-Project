# Question 2: Type Casting and Average 
# Question: Take three numbers as input (they may contain decimal values). Convert them to float using type casting and print
#  their average rounded to 2 decimal places. 
# Input: 
# 12.5 
# 15 
# 17.5 
 
# Output: 
# 15.00
num1 = float(input("Enter the frist value : "))
num2 = float(input("Enter the second value : "))
num3 = float(input("Enter the third value : "))

average = (num1 + num2 + num3) /3

print("Average = ", format(average, ".2f"))