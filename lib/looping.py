#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # for i in range(10):
    #     print(10 - i)
    #     if i == 1:
    #         print("Happy New Year!")
    count=10
    while count > 0:
        print(count)
        count = count-1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    # list compreheension
    return [i**2 for i in int_list]
   


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    
