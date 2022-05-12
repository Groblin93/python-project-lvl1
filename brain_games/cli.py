"""functions for interactions with user."""

import prompt


def welcome_user(logger):
    """Ask name user and write greetings for user.

    Args:
        logger: return registrator
    """
    name = prompt.string('May I have your name? ')
    logger.warning('{b}{a}{c}'.format(a=name, b='Hello, ', c='!'))
