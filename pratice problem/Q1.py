# Question 1: Largest of Three Numbers 
# Question: Write a program that takes three integers as input and prints the largest among them 
# using conditional statements. 
# Input: 
# 15 
# 27 
# 19 
 
# Output: 
# 27 
 

a = 15
b = 27
c = 19

if a > b and a > c:
    result = a
    print("a is maximum number")

elif b > a and b > c:
    result = b
    print("b is maximum number")

else:
    result = c
    print("c is maximum number")

print(result)