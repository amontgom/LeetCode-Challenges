# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:47:08 2018

@author: Aaron Taylor


LeetCode Problems: Hamming Distance

The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits
are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        binx = list('{:031b}'.format(x))
        biny = list('{:031b}'.format(y))
        count = 0
        for i in range(31):
            if binx[i] != biny[i]:
                count+=1
        return count