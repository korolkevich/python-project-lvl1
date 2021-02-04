"""Сборный модуль."""
from brain_games import cli


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
