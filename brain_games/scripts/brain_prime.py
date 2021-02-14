"""Game. Find prime number."""
from random import randint

from brain_games.scripts import brain_games as sc


def is_prime(num):
    """Calculate given number is prime.

    Args:
        num: given number.

    Returns:
        Boolean values prime or not.
    """
    if num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor * divisor <= num and num % divisor != 0:
        divisor += 2
    return divisor * divisor > num


def statement_generation():
    """Statement of the task condition.

    Returns:
        question_arg: Random number.
        correct_answer: True if prime else False.
    """
    end = 2500
    question_arg = randint(2, end)  # noqa:S311
    correct_answer = 'yes' if is_prime(question_arg) else 'no'
    return question_arg, correct_answer


def main():
    """Game flow."""
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
