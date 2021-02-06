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
    print('Find the greatest common divisor of given numbers.')
    return name


def calculation(a, b):
    if a == 0 or b == 0: return max(a, b)
    if a >= b: return calculation(a % b, b)
    if b >= a: return calculation(a, b % a)


def ask_question():
    """Проверяет результаты ответов.

    Returns:
        Correct answer
        User answer
    """
    number_one = randint(1, 100)  # noqa:S311
    number_two = randint(1, 100)  # noqa:S311
    correct_answer = calculation(number_one, number_two)
    print('Question: {0} {1}'.format(number_one, number_two))
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
