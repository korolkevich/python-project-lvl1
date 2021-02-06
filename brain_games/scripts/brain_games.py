"""Сборный модуль."""
from brain_games import cli


def main():
    """Привествует в игре, а затем делает персональное привествие.

    Returns:
        Name user.
    """
    print('Welcome to the Brain Games!')
    return cli.welcome_user()


if __name__ == '__main__':
    main()
