# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same_node(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            if node1.val != node2.val:
                return False
            if not is_same_node(node1.left, node2.left):
                return False
            if not is_same_node(node1.right, node2.right):
                return False
            return True
        return is_same_node(p, q)

# Approach
# - Recursively check each node
# - Check if both node are null -> Same
# - Check if one of the node is null -> Different
# - Check if val of both node is same or different
# - Recusively call for left and right child

# Time Complexity
# - Visit each node: O(n)

# Space Complexity
# - Recursion stack: O(min(m,n))
