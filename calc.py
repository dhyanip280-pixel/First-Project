def calculator(num1,num2,operator):
    try :

        if operator == "+": # condition
            result = num1 + num2 # Use of operator
            print ("Answer =", result) # output

        elif operator == "-": # condition
            result = num1 - num2 # Use of operator
            print("Answer =",result) # output

        elif operator == "*": #condition
            result = num1 * num2 # Use of operator
            print("Answer =",result) # output

        elif operator == "/": # condition 
            if num2 != 0: #condition is zero does not equal to zero
                result = num1 / num2 # operator
                print("Answer =",result) #output
            else :# false condition
                print("Cannot divide by zero") #output

        else : # false condition
            print("Invalid operator") # output
    except ValueError :
        print("invalid Input")