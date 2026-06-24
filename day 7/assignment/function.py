# calculator:


def calculator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print(f"Please use the selected operator only '{operator}' is invalid ")


while True:
    try:
        num1 = int(input("Enter the first number: "))
        operator = input("Enter the operator: ")
        num2 = int(input("Enter the second number: "))
        calculator(num1, num2, operator)

    except Exception as e:
        print("Error :", e)

    choice = input("Do you want to continue again (y/n): ")
    if choice == "n":
        break


