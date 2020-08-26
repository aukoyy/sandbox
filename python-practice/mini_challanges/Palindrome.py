# Solve palindrome
# if it is, return input
# if it isn't, add the reverse of the maybePalindrome number to the maybePalindrome
# and check again. If it is, return palindrome

def reverseInteger(num1):
    reversedVariable = list(str(num1))
    reversedVariable.reverse()
    return int(''.join(reversedVariable))


def isPalindrome(variable):
    return variable == reverseInteger(variable)


def palindromeMachine(startVariable):
    if isPalindrome(startVariable):
        return startVariable
    else:
        try:
            newTestNumber = startVariable + reverseInteger(startVariable)
            return palindromeMachine(newTestNumber)
        except:
            return -1


result = palindromeMachine(12)
print(result)
