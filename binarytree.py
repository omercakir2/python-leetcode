#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        ldepth=self.maxDepth(root.left)
        rdepth=self.maxDepth(root.right)
        return max(ldepth,rdepth)+1
#[3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculating the maximum depth
solution = Solution()
maxi = solution.maxDepth(root)
print(maxi)