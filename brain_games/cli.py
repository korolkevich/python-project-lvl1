"""Модуль с функцией разговорником."""
import prompt


def welcome_user():
    """Справшивает у пользователя его имя, а затем приветсвует его.

    Returns:
        User name.
    """
    name = prompt.string('May I have your name? ')
    text = 'Hello, {0}'.format(name)
    print(text)
    return name
