"""Game. Find the greatest common divisor."""
from random import randint

from brain_games.scripts import brain_games as sc


def calculation(num_a, num_b):
    """Find the greatest common divisor of given numbers.

    Args:
        num_a: First number.
        num_b: Second number.

    Returns:
        Greatest common divisor of given numbers.
    """
    if num_a == 0 or num_b == 0:
        return max(num_a, num_b)
    elif num_a >= num_b:
        return calculation(num_a % num_b, num_b)
    elif num_b >= num_a:
        return calculation(num_a, num_b % num_a)


def statement_generation():
    """Statement of the task condition.

    Returns:
        question_arg: Random number.
        correct_answer: True if prime else False.
    """
    number_one = randint(1, 100)  # noqa:S311
    number_two = randint(1, 100)  # noqa:S311
    correct_answer = calculation(number_one, number_two)
    question_arg = '{0} {1}'.format(number_one, number_two)
    return question_arg, correct_answer


def main():
    """Game flow."""
    rules = 'Find the greatest common divisor of given numbers.'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
