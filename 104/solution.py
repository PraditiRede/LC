# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def find_depth(node, height):
        #     if not node:
        #         return height
        #     return max(find_depth(node.left, height+1), find_depth(node.right, height+1))
        # return find_depth(root, 0)

        if not root:
            return 0
        queue = deque()
        queue.append(root)
        height = 0
        while queue:
            height += 1
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return height

# Approach
# - Recursively call for left and right child if exists
# - Maintain height and return max of each child
# OR
# - Traverse the tree level by level using BFS and maintain height
# - Return height after traversing all levels

# Time Complexity
# - Visit each node: O(n)

# Space Complexity
# - O(h) where h is the height of the tree
# - Queue for BFS: O(w) where w is the width of the tree
