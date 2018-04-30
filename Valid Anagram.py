# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:57:17 2018

@author: Aaron Taylor


LeetCode Problems: Valid Anagram

Given two strings s and t, write a function to determine if t is an
anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt
your solution to such case?
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0]*123
        for i in s:
            count[ord(i)] += 1
        for j in t:
            if count[ord(j)] == 0:
                return False
            count[ord(j)] -= 1
        return True