# 

def fizz_buzz(num1):
    output = ''
    if num1 % 3 == 0:
        output += 'Fizz'
    if num1 % 5 == 0:
        output += 'buzz'
    if output == '':
        output = 'Something else'

    return output


result = fizz_buzz(15)
print(result)