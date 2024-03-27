def writeToFile(filename, text):
    with open(filename, 'w') as fileObj:
        fileObj.write(text)

def appendToFile(filename, text):
    with open(filename, 'a') as fileObj:
        fileObj.write(text)

def readFromFile(filename):
    with open(filename, 'r') as fileObj:
        return fileObj.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
print(readFromFile('greet.txt'))

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
