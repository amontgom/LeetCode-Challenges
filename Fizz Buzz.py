# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 13:30:27 2018

@author: Aaron Taylor


LeetCode Problems: Fizz Buzz

Write a program that outputs the string representation of numbers
from 1 to n.

But for multiples of three it should output “Fizz” instead of the
number and for the multiples of five output “Buzz”. For numbers which
are multiples of both three and five output “FizzBuzz”.
"""

class Solution(object):
    def fizzBuzz(self, n):
        nmbrs = list()
        for x in range (1, n+1):
            if(x%3 == 0 and x%5 != 0):
                nmbrs.append('Fizz')
            elif(x%3 != 0 and x%5 == 0):
                nmbrs.append('Buzz')
            elif(x%3 == 0 and x%5 == 0):
                nmbrs.append('FizzBuzz')
            else:
                nmbrs.append(str(x))
        return nmbrs