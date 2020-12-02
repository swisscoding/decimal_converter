#!/usr/local/bin/python3

import colored

print(colored.stylize("\n---- | Convert binary to decimal | ----\n", colored.fg("red")))

def binary(l):
    new_num = l[0] * 2
    l.insert(0, new_num)
    return l

number = input("Type in a binary number: ")

binaryNumber = [1]
new_number = 0

while len(binaryNumber) != len(number):
    binary(binaryNumber)

number_list = []
for i in number:
    number_list.append(i)

count = 0
for i in number_list:
    new_number += int(i) * binaryNumber[count]
    count += 1

print(f"The decimal number is: {new_number}\n")
