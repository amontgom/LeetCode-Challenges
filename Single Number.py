# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:56:47 2018

@author: Aaron Taylor


LeetCode Problems: Single Number

Given a non-empty array of integers, every element appears twice
except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution(object):
    def singleNumber(self, nums):
        nums2 = []
        for i in range(len(nums)):
            if nums[i] in nums2:
                nums2.remove(nums[i])
            else:
                nums2.append(nums[i])
        return nums2[0]
    
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)