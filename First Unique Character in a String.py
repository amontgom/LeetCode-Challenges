# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:47:26 2018

@author: Aaron Taylor


LeetCode Problems: First Unique Character in a String

Given a string, find the first non-repeating character in it and
return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        count = [0]*123
        letters = []
        indices = []
        for i in s:
            count[ord(i)] += 1
        for j in range(len(count)):
            if count[j] == 1:
                letters.append(j)
        for k in range(len(letters)):
            letters[k] = chr(letters[k])
        for l,val in enumerate(s):
            if val in letters:
                indices.append(l)
        if not indices:
            return -1
        else:
            return min(indices)