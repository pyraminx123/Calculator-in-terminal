# pyraminx123

print("""The operators allowed are:
+ for addition
- for substraction
* for multyplication
/ for divition

Note that you can only input operations with only two values.

""")

calculate = True

while calculate == True:
    operation = input("Enter a simple math operation: ")

    values = operation.split(" ")

    value1 = values[0]
    operator = values[1]
    value2 = values[2]

    def basic_operation(op, v1, v2):
        return eval(f'{v1}{op}{v2}')


    print(basic_operation(operator, value1, value2))

    calculate = input("Do you want to calculate another math operation? [y/n] > ").lower()

    if calculate == "y":
        calculate = True
        print()
    elif calculate == "n":
        calculate = False
    else:
        calculate = False

# add an option for prime number
# fix " " (that it doesn't need space between v1, v2 and operator)
# try to find another solution than the eval() => not secure at all!!!
