"""Сборный модуль."""
from random import randint

from brain_games.scripts import brain_games as sc


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


def statement_generation():
    """Statement of the task condition.

    Returns:
        question_arg: Random number.
        correct_answer: True if prime else False.
    """
    operation = ['-', '+', '*'][randint(0, 2)]  # noqa:S311
    number_one = randint(1, 100)  # noqa:S311
    number_two = randint(1, 100)  # noqa:S311
    correct_answer = calculation(number_one, number_two, operation)
    question_arg = '{0} {1} {2}'.format(number_one, number_two, operation)
    return question_arg, correct_answer


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    rules = 'What is the result of the expression?'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
