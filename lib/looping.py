#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    i = 10
    while i >= 1:
        print(i)
        if i == 1:
            print("Happy New Year!")
        i -= 1


def square_integers(int_list):
    # code goes here!
    int_list = [num * num for num in int_list]
    return int_list


def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
