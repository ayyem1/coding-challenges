class Solution:
    """
    Attempt 1
    Time Complexity: O(n^2) where n is length of nums
    Space Complexity: O(1) // Note: In Python2, range has a space complexity of O(n)
    """
    def removeElementAttemptOne(self, nums: list[int], val: int) -> int:
        # loop backwards through the array and push non-matches forward.
        numMatches = 0
        for i in range(len(nums) - 1, -1, -1):
            if (nums[i] != val):
                continue

            numMatches += 1
            for j in range(i + 1, len(nums)):
                nums[j - 1] = nums[j]

        return numMatches

    """
    Attempt 2
    Time Complexity: O(n) where n is length of nums
    Space Complexity: O(1) // Note: In Python2, range has a space complexity of O(n)
    """
    def removeElementAttemptTwo(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[index] = nums[i]
                index += 1

        return index

solution = Solution();
nums = [0,1,2,2,3,0,4,2]
result = solution.removeElementAttemptTwo(nums, 2)
print(result)
print(nums)
