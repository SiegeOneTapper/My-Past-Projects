print("Welcome to the Calculator")
print("Please Enter which action you wish to do")
print("1 for Add")
print("2 for Subtraction")
print("3 for Division")
print("4 for Multiply")
operation = input("Please Select what operation you wish to use ")
number1 = int(input("Please input the first number you wish to use "))
number2 = int(input("Please input the second number you wish to use "))

if operation == '1':
    number3 = number1 + number2
elif operation == '2':
    number3 = number1 - number2
elif operation == '3':
    number3 = number1 / number2
elif operation == '4':
    number3 = number1 * number2

print(number3)




        
           
