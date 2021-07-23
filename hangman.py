import random
from time import sleep
from img import img_dict


def set_up(word):
    return random.choice([letter for letter in word])


def display_word(word, guesses):
    show_word = ''
    for letter in word:
        if letter in guesses:
            show_word += letter
        else:
            show_word += '-'

    return show_word


def game():
    word = 'mailbox'
    guesses = [set_up(word)]
    game_on = True
    turn = 1
    print(img_dict[1])
    print()
    print(display_word(word, guesses))

    while game_on:
        answer = input('Pick a letter: ')

        while answer not in 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split():
            print('Must guess a letter of the alphabet')
            answer = input('Pick a letter: ')

        while answer in guesses:
            answer = input('Invalid guess\nTry Again:')
        guesses.append(answer)

        if answer not in word:
            turn += 1

        show_word = display_word(word, guesses)
        print(img_dict[turn])
        print()
        print('Guesses: {guess}\nTurns left {turn}:\n{word}'.format(turn=10 - turn, guess=guesses,word=show_word))
        print()
        if show_word == word:
            print('You win!')
            game_on = False

        if turn >= 9:
            game_on = False
            print(word)
            print('You lose')
        sleep(.5)


def replay():
    answer = input('Play Again?  [y/n]').lower()
    print(answer)
    while answer != 'y' and answer != 'n':
        answer = input('Invalid Answer please select y or n.\nPlay Again?  [y/n] ').lower()
    if answer == 'y':
        return True

    return False


running = True

while running:
    game()
    running = replay()
