"""Сборный модуль."""
from random import randint

import prompt

from brain_games.scripts import brain_games as sc


def is_prime(num):
    """Функция определения правильных чисел.

    Args:
        num: Входное число для проверки.
    Returns:
        True | False для данного числа.
    """
    if num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor * divisor <= num and num % divisor != 0:
        divisor += 2
    return divisor * divisor > num


def statement_generation():
    """Функуия поределения условия задачи.

    Return:
        question_arg: Random number.
        correct_answer: True if prime else False.
    """
    end = 2500
    question_arg = randint(2, end)  # noqa:S311
    correct_answer = 'yes' if is_prime(question_arg) else 'no'
    return question_arg, correct_answer


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
