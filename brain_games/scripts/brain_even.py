"""Game. Find even numbers."""
from random import randint

from brain_games.scripts import brain_games as sc


def statement_generation():
    """Statement of the task condition.

    Returns:
        question_arg: Random number.
        correct_answer: True if prime else False.
    """
    question_arg = randint(1, 100)  # noqa:S311
    correct_answer = 'yes' if question_arg % 2 == 0 else 'no'
    return question_arg, correct_answer


def main():
    """Game flow."""
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
