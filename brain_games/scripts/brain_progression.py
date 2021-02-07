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
    print('What number is missing in the progression?')
    return name


def statement_generation():
    start = randint(1, 25)  # noqa:S311
    length_regression = randint(5, 15)  # noqa:S311
    step = randint(2, 7)  # noqa:S311

    end = start + length_regression * step + 1
    regression = [x for x in range(start, end, step)]
    hide_index = randint(0, len(regression))  # noqa:S311
    hide_num = regression[hide_index]
    regression[hide_index] = '..'
    str_regression = str(regression)[1:-1]
    return str_regression, hide_num


def ask_question():
    """Проверяет результаты ответов.

    Returns:
        Correct answer
        User answer
    """

    regression, correct_answer = statement_generation()
    print('Question: {0}'.format(regression))
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
