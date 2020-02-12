#!/usr/bin/env python
import sys
import math


"""Implements math functions without using operators except for '+' and '-' """


__author__ = "github.com/knmavel"


def add(x, y):
    added = x + y
    return added


def multiply(x, y):
    multiplied = 0
    if x >= 0 and y >= 0:
        for counter in range(y):
            multiplied = add(multiplied, x)
        return multiplied
    if x <= 0 and y <= 0:
        for counter in range(-y):
            multiplied = add(multiplied, -x)
        return multiplied
    if x < 0 and y >= 0:
        for counter in range(y):
            multiplied = add(multiplied, x)
        return multiplied
    if x >= 0 and y < 0:
        for counter in range(x):
            multiplied = add(multiplied, y)
        return multiplied


def power(x, n):
    print(x**n)
    powered = 1
    for counter in range(n):
        powered = multiply(powered, x)
    return powered


def factorial(x):
    if x == 0:
        return 1
    for counter in range(x-1, 0, -1):
        x = multiply(x, counter)
    return x


def fibonacci(n):
    fib = [0, 1]
    for index in range(0, n):
        fib.append(fib[index]+fib[index+1])
    return fib[n]


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
        print(add(int(numbers[0]), int(numbers[1])))
    elif option == '--multiply':
        print(multiply(int(numbers[0]), int(numbers[1])))
    elif option == '--power':
        print(power(int(numbers[0]), int(numbers[1])))
    elif option == '--factorial':
        print(factorial(int(numbers[0])))
    elif option == '--fibonacci':
        print(fibonacci(int(numbers[0])))
    else:
        print ('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
