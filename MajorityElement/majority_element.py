"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
class Solution:
    """
    Time Complexity: O(nlog(n)) where n is the number of elements in nums. This also varies based on the sorting
    algorithm.
    Space Complexity: O(1)
    """
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[(len(nums) // 2)]