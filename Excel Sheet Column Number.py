# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:54:57 2018

@author: Aaron Taylor


LeetCode Problems: Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its
corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution(object):
    def titleToNumber(self, s):
        step = 1
        column = 0
        for i in s[::-1]:
            column += (int(i, 36) - 9)*step
            step *= 26
        return column