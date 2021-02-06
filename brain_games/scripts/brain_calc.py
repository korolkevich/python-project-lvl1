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
    print('What is the result of the expression?')
    return name


def calculation(number_one, number_two, operation):
    """Производит математические операции.

    Args:
        number_one: Number one who be calculated.
        number_two: Number two who be calculated.
        operation: Math operation with two numbers.

    Returns:
        Calculated correct answer
    """
    if operation == '+':
        return number_one + number_two
    elif operation == '-':
        return number_one - number_two
    elif operation == '*':
        return number_one - number_two


def ask_question():
    """Проверяет результаты ответов.

    Returns:
        Correct answer
        User answer
    """
    operation = ['-', '+', '*'][randint(0, 2)]  # noqa:S311
    number_one = randint(1, 100)  # noqa:S311
    number_two = randint(1, 100)  # noqa:S311
    correct_answer = calculation(number_one, number_two, operation)
    print('Question: {0} {1} {2}'.format(number_one, number_two, operation))
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
