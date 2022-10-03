num1 = int(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = int(input("Enter a number: "))

thisdict = {
    "+": num1 + num2,
    "-": num1 - num2,
    "/": num1 / num2,
    "*": num1 * num2,
    "^": num1 ** num2
}
if operator in thisdict:
    print(num1, operator, num2, "=", thisdict[operator])
else:
    print("Error", operator, "is not a valid operator")
