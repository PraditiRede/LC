class Solution:
    def check(self, nums: List[int]) -> bool:
        # new_arr = sorted(nums)
        # n = len(new_arr)
        # for i in range(n):
        #     temp_arr = new_arr[-i:] + new_arr[:-i]
        #     if temp_arr == nums:
        #         return True
        # return False

        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count += 1
        return count <= 1

# Approach
# - Sort the array
# - Try rotating the sorted array with all positions possible
# - Check if the rotated array is same as input array

# Time Complexity
# - Sorting an array: O(nlogn)
# - Rotating the array n times: O(n^2)
# - Overall Complexity: O(n^2)

# Space Complexity
# New array: O(n)
# Rotated Temporary array: O(n)
# Overall Complexity: O(n)
