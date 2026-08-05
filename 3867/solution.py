class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)

        curr_max = float('-inf')
        n = len(nums)
        prefixGcd = []
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            prefixGcd.append(gcd(nums[i], curr_max))
        prefixGcd.sort()

        res = 0
        left = 0
        right = len(prefixGcd) -1
        while left < right:
            res += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return res

# Approach
# - Maintain a curr maximuma and compute gcd of curr element and curr maximum and store in array
# - Sort the array of prefix GCDs
# - Use two pointers to compute the sum of GCDs of pairs from both ends

# Time Complexity
# - Compute GCD: O(log(max(nums)))
# - Sorting: O(nlogn)
# - Two pointer: O(n)
# - Overall Complexity: O(nlogn)

# Space Complexity
# - Prefix GCD array: O(n)
# - Overall Complexity: O(n)
