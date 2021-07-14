try:
    input1 = int(input('first number: '))
    input2 = input('operator (+, -, /, etc): ')
    input3 = int(input('last number: '))
    result = 0
    if "+" in input2:
        result = input1 + input3
    elif "-" in input2:
        result = input1 - input3
    elif "/" in input2:
        result = input1 / input3
    elif "*" in input2:
        result = input1 * input3

    print('result = ' + str(result) + '\n')

except:
    print("You Idiot you need to sepcify the number as 123 not as one, two three and operators only +,-,/,*")