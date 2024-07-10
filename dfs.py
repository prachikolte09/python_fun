# def dfs(node):
#     # time complexity O(n)
#     #space O(n)
#     '''
#     Depth-First Search visits every node in a binary tree by going "down" as far as possible before backtracking to visit the nodes on the next path.
#     Depth-First Search is typically implemented as a recursive function. It visits new nodes in the tree by making recurisve calls. When a recursive call is made, a new call frame is pushed onto the call stack.
#     Backtracking occurs whenever a recursive call returns. The call frame is popped off the call stack, and execution returns to the next call frame on the call stack.
#     :param node:
#     :return:
#     '''
#
#     # base case
#     if not node:
#         return
#     #recursion
#     dfs(node.left)
#     dfs(node.right)


class Node:
    def __init__(self, value, left = None , right = None):
        self.value = value
        self.left = left
        self.right = right


#sum of the tree
def dfs(node):
    if node is None:
        return 0

    #base case
    if node.left is None and node.right is None:
        return node.val

    left = dfs(node.left)
    right = dfs(node.right)
    return left + right + node.val


def findmaxsbutree(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.val

    left = dfs(node.left)
    right = dfs(node.right)
    return max(left , right , node.val)





def findmaxdepth(node):
    if node is None:
        return 0


    left = findmaxdepth(node.left)
    right = findmaxdepth(node.right)
    return max(left, right) + 1

def targetpathsum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return target == root.val

    left = targetpathsum(root.left,target - root.val)
    right = targetpathsum(root.right,target - root.val)

    return left or right

