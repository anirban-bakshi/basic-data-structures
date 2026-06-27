'''
Problem

Given an array of integers, return the number of even integers.

Example:

Input:
[3, 8, 2, 10, 5]

Output:
3
'''

from typing import List

class Solution:

    def count_even(self, list: List[int]) -> int:

        count = 0

        if len(list) == 0:
            return count
        
        for num in list:
            if num%2 == 0:
                count = count + 1

        return count
    
s = Solution()
print(s.count_even([3, 8, 2, 10, 5]))