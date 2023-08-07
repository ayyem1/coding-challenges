"""
PROBLEM
Implement an algorithm to determine if a string has all unique characters.

Follow Up:
What if you cannot use additional data structures?
"""


class Solution:
    """
    Args:
        s (string): string of characters

    Returns: (bool): True if the given string has no repeating characters.

    Time Complexity: O(nlog(n))
    Space Complexity: O(n)
    """

    @staticmethod
    def is_unique(s: str) -> bool:
        uniqueStr = set(s)
        return len(uniqueStr) == len(s)

    """
    In this implementation we assume the string is composed of ascii characters (256 chars)
    Args:
        s (string): string of ascii characters

    Returns: (bool): True if the given string has no repeating characters.

    Time Complexity: O(n) Arguably, this can be constant as well since we'll never iterate more than 256 times.
    Space Complexity: O(1) We will only ever create an array of size 256.
    """
    MAX_CHAR = 256

    def is_unique_ascii(self, s: str) -> bool:
        n = len(s)
        if n > self.MAX_CHAR:
            return False

        charsCache = [False] * self.MAX_CHAR
        for i in range(n):
            if charsCache[ord(s[i])]:
                return False
            charsCache[ord(s[i])] = True

        return True

    """
    In this implementation we assume the string is composed of lower case letters [a-z].
    We will not use any data structures.
     
    Args:
        s (string): string of ascii characters

    Returns: (bool): True if the given string has no repeating characters.

    Time Complexity: O(n) Arguably, this can be constant as well since we'll never iterate more than 256 times.
    Space Complexity: O(1) We will only ever create an array of size 256.
    """

    @staticmethod
    def is_unique_no_datastructure(s: str) -> bool:
        # 32 bit int that should be enough for the 26 letters we're validating.
        checker = 0
        for i in range(len(s)):
            # Determine the bit in checker for this character.
            bitIndex = ord(s[i]) - ord('a')

            # If the bit has already been set, we have a duplicate.
            if checker & (1 << bitIndex) > 0:
                return False

            # Set the bit for future checks.
            checker |= 1 << bitIndex

        # No duplicates!
        return True


print(Solution.is_unique(""))
print(Solution.is_unique("a"))
print(Solution.is_unique("water"))
print(Solution.is_unique("hello"))

solution = Solution()
print(solution.is_unique_ascii(""))
print(solution.is_unique_ascii("a"))
print(solution.is_unique_ascii("water"))
print(solution.is_unique_ascii("hello"))

print(Solution.is_unique_no_datastructure(""))
print(Solution.is_unique_no_datastructure("a"))
print(Solution.is_unique_no_datastructure("water"))
print(Solution.is_unique_no_datastructure("hello"))