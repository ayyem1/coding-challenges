"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    """
    This solution caches the last k elements, shifts over the first n - k elements,
    and appends the cached elements.
    Args:
        nums (list[int]): list of numbers to be rotated

    Returns: (None): Modify nums in-place instead.

    Time Complexity: O(n + k)
    Space Complexity: O(k)
    """
    def rotate(self, nums: list[int], k: int) -> None:
        if k <= 0:
            return
        n = len(nums)
        k %= n

        stored_values = [0] * k
        index = 0
        for i in reversed(range(n)):
            if i >= len(nums) - k:
                stored_values[index] = nums[i]
                index += 1
            else:
                nums[i + k] = nums[i]

        # Add stored values back into nums.
        # Note: Stored values are in reverse order.
        for j in range(k):
            nums[j] = stored_values[k - j - 1]

    """
    This solution grabs the window defined by [0, n - k] and shifts it over k times.
    Args:
        nums (list[int]): list of numbers to be rotated

    Returns: (None): Modify nums in-place instead.

    Time Complexity: O(nk)
    Space Complexity: O(1)
    """
    def rotateSecondOption(self, nums: list[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)

        window_size = len(nums) - k
        for i in range(window_size, len(nums)):
            value = nums[i]
            for j in reversed(range(i - window_size, i)):
                nums[j + 1] = nums[j]
            nums[(i + k) % len(nums)] = value

    """
    This solution does the following:
    1. Reverse the elements in range [0, n - k]
    2. Reverse the elements in range [n - k, n]
    3. Reverse the entire list
    Args:
        nums (list[int]): list of numbers to be rotated

    Returns: (None): Modify nums in-place instead.

    Time Complexity: O(nk)
    Space Complexity: O(1)
    """
    def rotateThirdOption(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums: list[int], start: int, end: int):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

solution = Solution()

test1 = [1, 2, 3, 4, 5, 6, 7]
solution.rotateThirdOption(test1, 3)
print(test1)

test2 = [-1, -100, 3, 99]
solution.rotateThirdOption(test2, 2)
print(test2)
