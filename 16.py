def mode(numbers):
    numberCount = {}
    mostFreqNumber = None
    mostFreqNumberCount = 0
    if len(numbers) == 0:
        return None
    for i in numbers:
        if i not in numberCount:
            numberCount[i] = 0
        numberCount[i] += 1
        if numberCount[i] > mostFreqNumberCount:
            mostFreqNumber = i
            mostFreqNumberCount = numberCount[i]
    return mostFreqNumber

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4
