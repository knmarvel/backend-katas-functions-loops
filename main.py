#!/usr/bin/env python
import sys


"""Implements math functions without using operators except for '+' and '-' """


__author__ = "github.com/knmavel"


def add(x, y):
    print(x, y)
    return x + y


def multiply(x, y):
    print(x, y)
    return x*y


def power(x, n):
    print(x, n)
    return x**n


def factorial(x):
    print(x)
    return math.factorial(x)


def fibonacci(n):
    print (n)
    return (str(n) + " ain't no easy check for fibbers")



def main():
    if len(sys.argv) < 3:
        print ('usage: python main.py {--add | --multiply | --power | --factorial | fibonacci } {[x ,y] | [x, y] | [x, n] | [x] | [n]  ')
        sys.exit(1)
    if sys.argv[0] == "--add" or sys.argv[0] == "--multiply" or sys.argv[0] == "--power":
        if len(sys.argv) != 5:
            print("need two integer arguments for that function")
    else:
        if len(sys.argv) != 4:
            print("need one integer parameter for that function")

    option = sys.argv[1]
    numbers = sys.argv[2:]
    if option == '--add':
        add(int(numbers[0]), int(numbers[1]))
    elif option == '--multiply':
        multiply(numbers)
    elif option == '--power':
        power(numbers)
    elif option == '--factorial':
        factorial(numbers)
    elif option == '--fibonacci':
        fibonacci(numbers)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()