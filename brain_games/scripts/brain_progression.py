"""Сборный модуль."""
from random import randint

from brain_games.scripts import brain_games as sc


def generate_progression():
    """Generate random progression.

    Returns:
        Random progression.
    """
    statement = {
        'start_min': 1,
        'start_max': 25,
        'size_min': 5,
        'size_max': 15,
        'step_min': 2,
        'step_max': 7,
    }
    start = randint(statement['start_min'], statement['start_max'])  # noqa:S311
    length_regression = randint(  # noqa: S311
        statement['size_min'],
        statement['size_max'],
    )
    step = randint(statement['step_min'], statement['step_max'])  # noqa:S311

    end = start + length_regression * step + 1
    return list(range(start, end, step))


def statement_generation():
    """Statement of the task condition.

    Returns:
        question_arg: Random progression.
        correct_answer: hid number.
    """
    regression = generate_progression()
    hide_index = randint(0, len(regression))  # noqa:S311
    correct_answer = str(regression[hide_index])
    regression[hide_index] = '..'
    question_arg = str(regression)[1:-1]
    return question_arg, correct_answer


def main():
    """Game flow."""
    rules = 'What number is missing in the progression?'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
