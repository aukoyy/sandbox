input1 = 'Temeria'
input2 = 'IT'


def third_letter(input):
    letterArray = list(input)
    if len(letterArray) < 3:
        return 'q'
    else:
        return letterArray[2]


result = third_letter(input1)
print(result)
