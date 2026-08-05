class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Return an array with each element representing the rank of elements in the original array.
        """
        new_arr = sorted(arr)
        rank_map = {}
        rank = 1
        for i in range(len(new_arr)):
            if new_arr[i] not in rank_map:
                rank_map[new_arr[i]] = rank
                rank += 1
        for i in range(len(arr)):
            arr[i] = rank_map[arr[i]]
        return arr

# Approach
# - Copy the array into a new arry and sort it
# - Traverse the sorted array while assigning rank to each unique element
# - Traverse the original array while replacing the elements with it's corresponsing rank from the rank_map

# Time Complexity
# - Copying/sorting the array: O(nlogn)
# - Building rank_map: O(n)
# - Replacing original array with ranks: O(n)
# - Overall Complexity: O(nlogn)

# Space Complexity
# - new_arr stores copy of arr: O(n)
# - rank_map stores n elements in worst case: O(n)
# - Overall Complexity: O(n)
