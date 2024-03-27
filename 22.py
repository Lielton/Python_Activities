def rpsWinner(player1, player2):
    choice = ['rock', 'paper', 'scissors']
    if player1 not in choice or player2 not in choice:
        return 'error'
    if player1 == 'rock':
        if player2 == 'scissors':
            return 'player one'
        elif player2 == 'paper':
            return 'player two'
        else:
            return 'tie'
    elif player1 == 'paper':
        if player2 == 'scissors':
            return 'player two'
        elif player2 == 'rock':
            return 'player one'
        else:
            return 'tie'
    else:
        if player2 == 'scissors':
            return 'tie'
        elif player2 == 'paper':
            return 'player one'
        else:
            return 'player two'

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('rock', 'dog') == 'error'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'
