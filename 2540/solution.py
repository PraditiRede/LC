class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while ptr1 < n1 and ptr2 < n2:
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
        return -1

# Approach
# - Start with two pointers pointing the first element of each array
# - If both pointers have same value return that value
# - If one of the pointers vale is less than another increment that pointer (works because arays are in ascending order i.e increasing order)

# Time Complexity
# - Alternating pointers iterate at the most m+n time: O(m+n)

# Space Complexity
# - Pointers and array lengths are only stored, thus, O(1)