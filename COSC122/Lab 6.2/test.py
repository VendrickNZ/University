def findClosestValueInBst(tree, target):

    bestgap = abs(target - tree.value)
    currentTree = tree
    previous = tree
    if tree.value == target:
        return tree.value
    

    if target < currentTree.value:
        currentTree = currentTree.left
        gap = abs(target - currentTree.value)
        if gap < bestGap:
            bestGap = gap

    else:
        currentTree = currentTree.right
        gap = abs(target - currentTree.value)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None