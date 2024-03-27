def convertToFahrenheit(degreesCelsius):
    degreesFahrenheit = (degreesCelsius * 9 /5) + 32
    return degreesFahrenheit

def convertToCelsius(degreesFahrenheit):
    degreesCelsius = (degreesFahrenheit - 32) * 5 / 9
    return degreesCelsius

x = True

while x:
    y = float(input("Gostaria de converter celsius para fahrenheit (digite 1), ou fahrenheit para celsius (digite 2)?"))

    if y == 1:
        degrees = float(input('Digite a temperatura'))
        newDegrees = convertToFahrenheit(degrees)
        print("Essa temperatura em Fahrenheit é " + str(newDegrees))
        input()
        x = False
        
    elif y == 2:
        degrees = float(input('Digite a temperatura'))
        newDegrees = convertToCelsius(degrees)
        print("Essa temperatura em Fahrenheit é " + str(newDegrees))
        input()
        x = False
    else:
        y = input("Gostaria de converter celsius para fahrenheit (digite 1), ou fahrenheit para celsius (digite 2)?")

    assert convertToCelsius(0) == -17.77777777777778

    assert convertToCelsius(180) == 82.22222222222223

    assert convertToFahrenheit(0) == 32

    assert convertToFahrenheit(100) == 212

    assert convertToCelsius(convertToFahrenheit(15)) == 15

    assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
