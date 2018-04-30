# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:39:25 2018

@author: Aaron Taylor


LeetCode Problems: Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        numsS = set(nums)
        if len(nums) != len(numsS):
            return True
        else:
            return False