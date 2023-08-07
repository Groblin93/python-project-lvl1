#!/usr/bin/env python3
import random
import prompt

ROUND_NUMBERS = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < ROUND_NUMBERS:
        number = random.randint(1, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer != 'yes':
            print(answer, "is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, ", name)
            break
        elif number % 2 != 0 and answer != 'no':
            print(answer, "is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, ", name)
            break
        else:
            print('Correct!')
            i += 1
    if i == 3:
        print('Congratulations, ' + name + '!')


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    check_even(name)


if __name__ == '__main__':
    main()
