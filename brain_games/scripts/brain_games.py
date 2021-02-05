"""Сборный модуль."""
from brain_games import cli


def main():
    """Привествует в игре, а затем делает персональное привествие."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
