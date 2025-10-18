import click
import english_words
import re


DICTIONARY = english_words.get_english_words_set(["web2"], lower=True)


def validate_letters(ctx, param, value: str):
    value = value.lower()
    if re.match("[a-z]{7}", value):
        return value
    raise click.BadParameter(f"Not 7 letters: {value}")


@click.command()
@click.argument("letters", callback=validate_letters)
def solve(letters: str):
    """LETTERS should contain the 7 spelling bee letters, with the middle letter first"""
    letters = letters.lower()
    letter_set = set(letters)
    valid_words = sorted(
        [
            word
            for word in DICTIONARY
            if len(word) >= 4
            and word.startswith(letters[0])
            and not set(word) - letter_set
        ],
        key=len,
    )
    for word in valid_words:
        print(word)


if __name__ == "__main__":
    solve()
