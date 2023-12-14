class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def verticalTraversal(root):
    if not root:
        return []
    
    m = {}
    queue = ([(root, 0, 0)])

    while queue:
        node, hd, level = queue.pop(0)

        if hd in m:
            m[hd].append((node.key, level))
        else:
            m[hd] = [(node.key, level)]

        if node.left:
            queue.append((node.left, hd - 1, level + 1))
        if node.right:
            queue.append((node.right, hd + 1, level + 1))

    result = []
    for node, nodes in sorted(m.items()):
        result.extend([key for key, node in sorted(nodes)])

    return result

def verticalTraversalReversed(root):
    return verticalTraversal(root)[::-1]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(9)

    print("Vertical order traversal is:", verticalTraversal(root))
    print("Reversed output:", verticalTraversalReversed(root))
