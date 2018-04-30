# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 17:33:34 2018

@author: Aaron Taylor


LeetCode Problems: Missing Number

Given an array containing n distinct numbers taken from
0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could
you implement it using only constant extra space complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        sumN = sum(nums)
        sumM = sum(list(range(0,max(nums)+1)))
        diff = sumM - sumN
        if 0 not in nums:
            return 0
        elif (diff) == 0:
            return max(nums)+1
        else:
            return diff