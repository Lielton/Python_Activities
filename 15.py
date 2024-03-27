def median(numbers):
    numbers.sort()
    i = 0
    if len(numbers) == 0:
        return None
    elif len(numbers)%2 == 1:
        i = len(numbers)//2
        return numbers[i]
    else:
        i = ((len(numbers)/2) + ((len(numbers)/2)+1))/2
        return i

assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6
