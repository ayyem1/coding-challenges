#!/usr/bin/env python3
import sys
class PaidStairs:
    """
    Problem: Paid Staircase

	You are climbing a paid staircase. It takes n steps to reach to the top and you have to
	pay p[i] to step on the i-th stair. You can take [1,k] steps at any given time.
	What's the cheapest amount you have to pay to get to the top of the staircase?

    Time complexity: O(numStairs)
    Space complexity: O(numStairs)
    """
    def calculate(self, numStairs: int, maxStepCount: int, prices: [int]) -> int:
        if maxStepCount < 0: return 0

        resultsCache = [sys.maxsize] * (numStairs + 1)
        resultsCache[0] = 0
        for i in range(1, numStairs + 1):
            for k in range(1, maxStepCount + 1):
                if k > i:
                    break
                resultsCache[i] = min(resultsCache[i], resultsCache[i - k]);
            resultsCache[i] += prices[i]

        return resultsCache[numStairs]
