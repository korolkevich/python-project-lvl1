"""The Prefabricated module."""
import prompt

from brain_games import cli


def main():
    """Greets in-game and then makes a personalized greeting.

    Returns:
        Name user.
    """
    print('Welcome to the Brain Games!')
    return cli.welcome_user()


def ask_question(function):
    """Return the results of the responses.

    Args:
        function: The argument of the question.

    Returns:
        Correct answer.
        User answer.
    """
    question_arg, correct_answer = function()
    print('Question: {0}'.format(question_arg))
    answer = prompt.string('Your answer: ')
    return correct_answer, answer


def game_flow(name, statement_generation):
    """Run the game.

    Args:
        statement_generation: The condition generator function.
        name: Name player.
    """
    total_attempts = 3
    for attempt in range(0, total_attempts):  # noqa:WPS122
        correct_answer, answer = ask_question(statement_generation)
        if answer == correct_answer:
            print('Correct!')
            if attempt == 2:
                print('Congratulations, {0}!'.format(name))
        else:
            text = '"{0}" is wrong answer ;(. Correct answer was "{1}".'
            print(text.format(answer, correct_answer))
            break


def welcome(rules):
    """Welcomes you to the game, and then announces the rules of the game.

    Args:
        rules: Description of the game rules.

    Returns:
        Name user.
    """
    name = main()
    print(rules)
    return name


if __name__ == '__main__':
    main()
