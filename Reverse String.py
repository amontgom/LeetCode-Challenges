# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:02:37 2018

@author: Aaron Taylor


LeetCode Problems: Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        return s[::-1]