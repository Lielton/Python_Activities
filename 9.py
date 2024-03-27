def getChessSquareColor(column, row):
    if column % 2 == 0 and row % 2 == 0 and 0 <= column < 8 and 0 <= row < 8:
        return "white"
    elif column % 2 == 1 and row % 2 == 1 and 0 <= column < 8 and 0 <= row < 8:
        return "white"
    elif column % 2 == 0 and row % 2 == 1 and 0 <= column < 8 and 0 <= row < 8:
        return "black"
    elif column % 2 == 1 and row % 2 == 0 and 0 <= column < 8 and 0 <= row < 8:
        return "black"
    else:
        return ''


assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''
