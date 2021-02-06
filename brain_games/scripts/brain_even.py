"""Сборный модуль."""
from random import randint

import prompt

from brain_games.scripts import brain_games as sc


def welcome():
    """Привествует в игре, а затем объявляет правила игры.

    Returns:
        Name user.
    """
    name = sc.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def ask_question():
    """Проверяет результаты ответов.

    Returns:
        Correct answer
        User answer
    """
    random_number = randint(1, 100)  # noqa:S311
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    print('Question: {0}'.format(random_number))
    answer = prompt.string('Your answer: ')
    return correct_answer, answer


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    name = welcome()
    for attempt in range(0, 3):  # noqa:WPS122
        answer, correct_answer = ask_question()
        if answer == correct_answer:
            print('Correct!')
            if attempt == 2:
                print('Congratulations, {0}!'.format(name))
        else:
            text = '"{0}" is wrong answer ;(. Correct answer was "{1}".'
            print(text.format(answer, correct_answer))
            break


if __name__ == '__main__':
    main()
