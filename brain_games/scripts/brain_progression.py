"""Сборный модуль."""
from random import randint

# import prompt

from brain_games.scripts import brain_games as sc


def statement_generation():
    """Функуия определения условия задачи.

    Return:
        question_arg: Random progression.
        correct_answer: hid number.
    """
    start = randint(1, 25)  # noqa:S311
    length_regression = randint(5, 15)  # noqa:S311
    step = randint(2, 7)  # noqa:S311

    end = start + length_regression * step + 1
    regression = [x for x in range(start, end, step)]
    hide_index = randint(0, len(regression))  # noqa:S311
    correct_answer = regression[hide_index]
    regression[hide_index] = '..'
    question_arg = str(regression)[1:-1]
    return question_arg, correct_answer


# def ask_question():
#     """Проверяет результаты ответов.
#
#     Returns:
#         Correct answer
#         User answer
#     """
#
#     regression, correct_answer = statement_generation()
#     print('Question: {0}'.format(regression))
#     answer = prompt.string('Your answer: ')
#     return correct_answer, answer


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    rules = 'What number is missing in the progression?'
    name = sc.welcome(rules)
    sc.game_flow(name, statement_generation)


if __name__ == '__main__':
    main()
