# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:51:21 2018

@author: Aaron Taylor


LeetCode Problems: Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed
to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""
import operator
class Solution(object):
    def getSum(self, a, b):
        return operator.add(a,b)