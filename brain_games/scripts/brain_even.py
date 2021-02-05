"""Сборный модуль."""
import brain_games.scripts.brain_games as welcome
import prompt
from random import randint


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    welcome.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        random_number = randint(1, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        print('Question: {0}'.format(random_number))
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            if i == 2:
                print('Congratulations, Sam!')
        else:
            print(
                '\'{0}\' is wrong answer ;(. '
                'Correct answer was \'{1}\'.'.format(answer, correct_answer))
            break


if __name__ == '__main__':
    main()
