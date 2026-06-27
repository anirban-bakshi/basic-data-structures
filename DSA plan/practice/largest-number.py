'''
Problem

Given an array of integers,

Return the largest number.

Example

Input

[3,8,2,10,5]

Output

10

Restrictions:

Don't use Python's max().
Try to solve it in one traversal.
'''

from typing import List

class Solution:

    def find_largest(self, list: List[int]) -> int:
        if len(list) == 0:
            return -1
        largest = list[0]

        for num in list[1:]:
            if num > largest:
                largest = num

        return largest
    
s = Solution()
print(s.find_largest([3,8,2,10,5]))