class Solution:
    def createBinaryTree(self, d: List[List[int]]) -> Optional[TreeNode]:
        m: dict[int, TreeNode] = {}
        c: set[int] = set()
        for p, ch, l in d:
            if p  not in m: m[p]  = TreeNode(p)
            if ch not in m: m[ch] = TreeNode(ch)
            if l: m[p].left  = m[ch]
            else: m[p].right = m[ch]
            c.add(ch)
        return next(n for x, n in m.items() if x not in c)