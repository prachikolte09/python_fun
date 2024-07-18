'''
Since this question involves finding the shortest distance in a graph, we should use a breadth-first search (BFS) traversal to solve it.
BFS uses a queue to keep track of the nodes it needs to visit, and follows these steps:

Start at the root node and add it to the queue.
While the queue is not empty, remove the node at the front of the queue and visit it.
Add the children of the node to the back queue.
Repeat steps 2 and 3 until the queue is empty, which means you've processed all nodes in the tree.
'''

from collections import deque
#BFS is a traversal algorithm that visits all nodes at a particular level before moving to the next level.
#BFS uses a queue to keep track of the nodes it needs to visit.
def bfs(root):
    if not root:
        return None

    result = []
    queue = deque([root])

    while queue:
        # always remove left most element which was entered first O(1)
        curr_node = queue.popleft()
        # put the item at the right that's the last
        result.append(curr_node.val)

        # explore left neighbor then immediately right and push
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)