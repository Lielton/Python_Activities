def fizzBuzz(upTo):
    for i in range(1, upTo+1):
        if i % 3 == 0 and not i % 5 == 0:
            print("Fizz", end=' ')

        elif i % 5 == 0 and not i % 3 == 0:
            print("Buzz", end=' ')

        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')

        else:
            print(i, end=' ')

x = int(input('Digite um número'))
fizzBuzz(x)
input()
