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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def statement_generation():
    start = randint(2, 2500)  # noqa:S311
    is_prime(start)
    correct_answer = 'yes' if is_prime(start) else 'no'
    return start, correct_answer


def ask_question():
    """Проверяет результаты ответов.

    Returns:
        Correct answer
        User answer
    """

    num, correct_answer = statement_generation()
    print('Question: {0}'.format(num))
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
