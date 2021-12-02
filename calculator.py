"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Enter your equation> ")
    token = user_input.split(' ')
    operator = token[0]
    result = None
    num1 = token[1]
    num2 = token[2]
    if operator == "q":
        break
    elif len(token)<2:
        print("It is not enough input")
    else:
        if operator == "+":
            result = add(num1,num2)
        elif operator == "-":
            result = subtract(num1, num2)
        
        elif operator == "*":
            result = multiply(num1, num2)
        
        elif operator == "/":
            result = divide(num1, num2)
        
        elif operator == "*":
            result = square(num1)
        
        elif operator == "**":
            result = cube(num1)
        
        elif operator == "**=":
            result = cube(num1, num2)
            
print(result)
