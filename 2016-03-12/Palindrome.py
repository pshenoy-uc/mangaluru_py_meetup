#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: 

Date : 12/03/16
"""

def fun_palindrome(number):

    str_n = str(number)
    rev_n = str(number)[::-1]

    if str_n == rev_n:
        return True
    else:
        return False


_number = input("Enter a Number:")


while True:
    if fun_palindrome(_number):
        print "%s is Palindrome" % _number
        break
    else:
        _number = _number +1

