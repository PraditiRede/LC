class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # k = len(nums) - k
        # for i in range(k):
        #     nums.append(nums[i])
        # for i in range(k):
        #     nums.pop(0)

        # n = len(nums)
        # k = k % n
        # for i in range(k):
        #     x = nums.pop()
        #     print(x)
        #     nums.insert(0, x)

        # k = k % len(nums)
        # k = len(nums) - k
        # nums[:] = nums + nums[:k]
        # nums[:] = nums[k:]

        # k %= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]

        n = len(nums)
        k = k % n
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

# Approach
# - Reverse the entire array
# - Reverse first k element
# - Reverse the rest of the elements

# Time Complexity
# - Reverse entire array: O(n)
# - Reverse first k element: O(k)
# - Reverse the rest of the elements: O(n-k)
# - Overall Complexity: O(n)

# Space Complexity
# - O(1)
