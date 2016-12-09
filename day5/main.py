#!/usr/bin/env python

'''
Advent of Code 2016 - Day 5
Andre LeBlanc  (andre.leblanc@workiva.com)
'''

input = '''reyedfim'''

import hashlib

def part1():
    digits = ""
    ctr = 0
    while len(digits) < 8:
        hash = hashlib.md5(input + str(ctr)).hexdigest()
        if hash.startswith("00000"):
            digits += hash[5]
            print digits
        ctr += 1


def part2():
    digits = [" "] * 8
    ctr = 0
    while " " in digits:
        hash = hashlib.md5(input + str(ctr)).hexdigest()
        if hash.startswith("00000"):
            if hash[5].isdigit():
                pos = int(hash[5])
                if pos <= 7 and digits[pos] == " ":
                    digits[pos] = hash[6]
                    print ''.join(digits)
        ctr += 1



part1()
part2()

