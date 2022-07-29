def game():
    return 65


score = game()
with open('highScore.txt') as f:
    hiScore = f.read()

if hiScore=='':
    with open('highScore.txt', 'w') as f:
        f.write(str(score))

elif int(hiScore)<score:
    with open('highScore.txt', 'w')  as f:
          f.write(str(score))
    print('New high score!')
    
else:
    print('Not a new high score.')
    print('Your score:', score)
    print('High score:', hiScore)