"""Сборный модуль."""
import prompt

from brain_games import cli


def main():
    """Привествует в игре, а затем делает персональное привествие.

    Returns:
        Name user.
    """
    print('Welcome to the Brain Games!')
    return cli.welcome_user()


def ask_question(function):
    """Проверяет результаты ответов.

    Args:
        function: Аргумент вопроса.

    Returns:
        Correct answer.
        User answer.
    """
    question_arg, correct_answer = function()
    print('Question: {0}'.format(question_arg))
    answer = prompt.string('Your answer: ')
    return correct_answer, answer


def game_flow(name, statement_generation):
    """Функция определяющая правила игры.

    Args:
        statement_generation: функция генератор условия.
        name: Имя игрока.
    """
    total_attempts = 3
    for attempt in range(0, total_attempts):  # noqa:WPS122
        answer, correct_answer = ask_question(statement_generation)
        if answer == correct_answer:
            print('Correct!')
            if attempt == 2:
                print('Congratulations, {0}!'.format(name))
        else:
            text = '"{0}" is wrong answer ;(. Correct answer was "{1}".'
            print(text.format(answer, correct_answer))
            break


def welcome(rules):
    """Привествует в игре, а затем объявляет правила игры.

    Args:
        rules: Описание правил игры.

    Returns:
        Name user.
    """
    name = main()
    print(rules)
    return name


if __name__ == '__main__':
    main()
