"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
    1 <= nums.length <= 3 * 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

"""
class Solution(object):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) // NOTE: In Python2, range() has a space complexity of O(n)

    Args:
        nums (list[int]): A list of integer number
 
    Returns:
        int: The number of unique elements in the array with a maximum of one duplicate. So, this result could be at most 2*u where u is the number of unique numbers in the list.
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        for n in nums:
            if index < 2 or n != nums[index - 2]:
                nums[index] = n
                index += 1

        return index
    
solution = Solution()
test1 = [1,1,1,2,2,3]
result = solution.removeDuplicates(test1)
print(result)
print(test1)

test2 = [0,0,1,1,1,1,2,3,3]
result = solution.removeDuplicates(test2)
print(result)
print(test2)