def find_brackets(numberlist):
    openbracket = 0
    closebracket = 0
    bracket_opened = False
    for location in range(len(numberlist)):
        if numberlist[location] == "(":
            openbracket = location + 1
            bracket_opened = True
        if numberlist[location] == ")" and bracket_opened:
            closebracket = location
            bracket_opened = False
    return openbracket,closebracket


#% ddd
def find_operator(numberlist,operator):
    for location in range(len(numberlist)):
        if numberlist[location] == operator:
            return location

def compute(operator, numberlist):
    calculation_location = find_operator(numberlist,operator)
    num1 = numberlist[calculation_location-1]
    num2 = numberlist[calculation_location+1]
    numberlist.pop(calculation_location-1)
    numberlist.pop(calculation_location-1)
    if operator == "^":
        numberlist[calculation_location-1] = num1 ** num2
    if operator == "*":
        numberlist[calculation_location-1] = num1 * num2
    if operator == "/":
        numberlist[calculation_location-1] = num1 / num2
    if operator == "+":
        numberlist[calculation_location-1] = num1 + num2
    if operator == "-":
        numberlist[calculation_location-1] = num1 - num2
    return numberlist

def calculate_without_brackets(numberlist):

    while "^" in numberlist:
        numberlist = compute("^", numberlist)

    while "/" in numberlist:
        numberlist = compute("/", numberlist)

    while "*" in numberlist:
        numberlist = compute("*", numberlist)

    while "+" in numberlist:
        numberlist = compute("+", numberlist)

    while "-" in numberlist:
        numberlist = compute("-", numberlist)
    return numberlist


def parse_formula(calculation):
    numberlist = []
    number = ""
    counting = False
    for character in calculation:
        if character in ".1234567890":
            number += character
            counting = True
        else:
            if counting:
                numberlist.append(float(number))
                number = ""
                counting = False
            numberlist.append(character)
    if counting:
        numberlist.append(float(number))
    return numberlist

# # groups together the numbers and stores it in a list
# numberlist = parse_formula("5.5/3+4*7-6")
# calculate_without_brackets(numberlist)


# # numberlist = parse_formula("2*(3-4/(2+3))")

# print(numberlist)
def print_numberlist(numberlist):
    print(numberlist)
    print(" ".join([str(x) for x in numberlist]))
    return

def main():
    print("calculator")
    numberlist = input('Enter your formula:')
    numberlist = parse_formula(numberlist)
    print_numberlist(numberlist)
    

    while '(' in numberlist:
        openbracket,closebracket = find_brackets(numberlist)

        output = calculate_without_brackets(numberlist[openbracket:closebracket])
        del numberlist[openbracket-1:closebracket+1]
        numberlist.insert(openbracket-1, output[0])
        print_numberlist(numberlist)

    numberlist = calculate_without_brackets(numberlist)
    print_numberlist(numberlist)

if __name__ == "__main__":
    main()