"""The Prefabricated module."""
import prompt


def main():
    """Greets in-game and then makes a personalized greeting."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    text = 'Hello, {0}'.format(name)
    print(text)


if __name__ == '__main__':
    main()
