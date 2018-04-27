# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 13:48:02 2018

@author: Aaron Taylor


LeetCode Problems: Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left),
                       self.maxDepth(root.right)) + 1