class Solution:
    """
    Time Complexity: O(n) where n is length of nums
    Space Complexity: O(1) // NOTE: In Python2, range() has a space complexity of O(n)
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[index - 1]:
                nums[index] = nums[i]
                index += 1
        
        return index
    
    
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
numUnique = solution.removeDuplicates(nums)
print(numUnique)
print(nums)
