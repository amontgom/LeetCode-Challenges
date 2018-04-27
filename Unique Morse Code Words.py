# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:47:08 2018

@author: Aaron Taylor


LeetCode Problems: Unique Morse Code Words

International Morse Code defines a standard encoding where each letter
is mapped to a series of dots and dashes, as follows: "a" maps to
".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English
alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a
concatenation of the Morse code of each letter. For example, "cab"
can be written as "-.-.-....-", (which is the concatenation "-.-." +
"-..." + ".-"). We'll call such a concatenation, the transformation
of a word.

Return the number of different transformations among all words we
have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
 

Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""

import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        keys = list(string.ascii_lowercase)
        values = [".-","-...","-.-.","-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--","-.","---",".--.",
                 "--.-",".-.","...","-","..-","...-",".--","-..-",
                 "-.--","--.."]
        dictionary = dict(zip(keys,values))
        morse = list()
        for i in range(len(words)):
            word = list(words[i])
            morse.append("".join(list(map(dictionary.get, word))))
        morseset = set(morse)
        return len(morseset)
                
        
        