"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:

    """
    Attempt 1
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    def mergeAttemptOne(self, nums1: [int], m: int, nums2: [int], n: int) -> None:


        sortedList = []
        i = 0
        j = 0
        # Compare each item in the two lists and merge into sortedList
        while (i < m or j < n):
            if i < m and j < n:
                if (nums1[i] <= nums2[j]):
                    sortedList.append(nums1[i])
                    i += 1
                else:
                    sortedList.append(nums2[j])
                    j += 1
            elif i < m:
                sortedList.append(nums1[i])
                i += 1
            else:
                sortedList.append(nums2[j])
                j += 1

        # Copy over to nums1
        for k in range(m + n):
            nums1[k] = sortedList[k]

    """
    Attempt 2
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """
    def mergeAttemptTwo(self, nums1: [int], m: int, nums2: [int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if (i >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
    