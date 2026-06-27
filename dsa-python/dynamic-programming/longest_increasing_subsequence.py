# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some (or none) elements without changing the order of the remaining elements.

# Example

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: LIS is [2,3,7,101].

from typing import List

class LongestIncreasingSubsequence:

    def longest_subseq(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                pass