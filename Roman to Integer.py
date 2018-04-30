# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:07:52 2018

@author: Aaron Taylor


LeetCode Problems: Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X,
L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's
added together. Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not IIII. Instead, the number
four is written as IV. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which
is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed
to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        count = 0
        skip = 0
        for i, val in enumerate(list(s)):
            if val not in nums:
                return None
            if i == skip and i != 0:
                continue
            if val == "I":
                if i == len(s)-1:
                    count += 1
                    continue
                if s[i+1] == "V":
                    count += 4
                    skip = i + 1
                    continue
                elif s[i+1] == "X":
                    count += 9
                    skip = i + 1
                    continue
                else:
                    count += 1
                    continue
            elif val == "V":
                count += 5
                continue
            elif val == "X":
                if i == len(s)-1:
                    count += 10
                    continue
                if s[i+1] == "L":
                    count += 40
                    skip = i + 1
                    continue
                elif s[i+1] == "C":
                    count += 90
                    skip = i + 1
                    continue
                else:
                    count += 10
                    continue
            elif val == "L":
                count += 50
                continue
            elif val == "C":
                if i == len(s)-1:
                    count += 100
                    continue
                if s[i+1] == "D":
                    count += 400
                    skip = i + 1
                    continue
                elif s[i+1] == "M":
                    count += 900
                    skip = i + 1
                    continue
                else:
                    count += 100
                    continue
            elif val == "D":
                count += 500
                continue
            elif val == "M":
                count += 1000
                continue
        return count