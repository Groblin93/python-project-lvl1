#!/usr/bin/env python3
"""main package."""


import logging

from brain_games import cli


def main():
    """Launch mind games."""
    logger = logging.getLogger()
    logger.warning('Welcome to the Brain Games!')
    cli.welcome_user(logger)


if __name__ == '__main__':
    main()
