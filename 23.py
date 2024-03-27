x = 99

while x > 1:
    print(str(x) + ' ' + 'bottles of beer on the wall')
    print(str(x) + ' ' + 'bottles of beer,')
    print('Take one down,')
    print('Pass it around,')
    x -= 1
    print(str(x) + ' ' + 'bottles of beer on the wall,')
    print('')

if x == 1:
    print(str(x) + ' ' + 'bottles of beer on the wall')
    print(str(x) + ' ' + 'bottles of beer,')
    print('Take one down,')
    print('Pass it around,')
    x -= 1
    print('No more bottles of beer on the wall!')
