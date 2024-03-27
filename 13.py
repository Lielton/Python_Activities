def calculateSum(numbers):
    if len(numbers) == 0:
        return 0
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    return result

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840
