# // bfs using recursion in binary tree?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.bfs(root, 0, res)
        return res
        
    def bfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.bfs(root.left, level + 1, res)
        self.bfs(root.right, level + 1, res)