secret_word = 'rabbit'
guess = ''
guess_count = 0

while guess != secret_word:
    if guess_count < 3:
        guess = input('What is your guess?:')
        if guess==secret_word:
            print('You win!!!')
            break
    else:
        print('Out of Guessess!\nGame Over!')
        break
    guess_count += 1 