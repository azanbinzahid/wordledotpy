from random import randint
from termcolor import colored
from colorama import init
import os


def read_words(filename):
    """Read words from a file and return a list of words."""
    with open(filename, 'r') as f:
        return [line.strip().upper() for line in f]


def draw_state(words, ans):

    for word in words:
        print(colored(' | ', 'grey', 'on_white'), end='')
        for i, w in enumerate(word):
            clr = 'red' if w not in ans else 'green' if w == ans[i] else 'yellow'
            print(colored(w, clr, 'on_white'), end='')
            print(colored(' | ', 'grey', 'on_white'), end='')

        print()


def game(words):
    """Play a game of wordle."""

    ans = words[randint(0, len(words) - 1)]
    guess = 6
    user_input = []

    while guess:
        word = input().upper()
        os.system('clear')

        if len(word) != len(ans):
            print('Word must be {} letters long.'.format(len(ans)))
            draw_state(user_input, ans)
            continue

        user_input.append(word)
        draw_state(user_input, ans)

        if ans == word:
            break

        guess -= 1


words = read_words('dictionary.txt')
init()
game(words)
