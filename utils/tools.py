from random import (
    choice
)


def generate_random_string(min_len, alphabet):
    return ''.join([choice(alphabet) for _ in range(min_len)])
