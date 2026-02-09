def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {"+":add, "-":subtract, "*":multiply, "/":divide}
def calculator():
    number1 = int(input("Enter the first number: "))
    calc_again = True
    while calc_again:
        math_operation = input("Enter math operation +, -, * or /: ")
        number2 = int(input("Enter the second number: "))

        result = operations[math_operation](number1, number2)

        print(f"{number1} {math_operation} {number2} = {result}")
        answer = input("Do you want to continue calculating? Press Yes or No:").lower()
        if answer == "yes":
            number1 = result
        else:
            calc_again = False
            calculator()
calculator()



