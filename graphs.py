#DFS for a graph is conceptually similar to DFS on a binary tree.
'''
adjacency list
allows lookup O(1)
'''

'''
Each node can have any amount of neighbors, so we need a for loop to iterate over each neighbor rather than making calls to the left and right children of the current node.
Because graphs can contain cycles, we need to keep track of nodes we have already visited. If we encounter a node that has already been visited, we should return immediately without making any further recursive calls (or skip it in the loop altogether). Otherwise, we may end up in an infinite loop.
We don't need an explicit base case like we do in the trees. Eventually, we will visit all nodes in the graph, and the recursion will stop on its own (with the help of the visited set).
'''
n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]

def build_adj_list(n,edges):
    adj_list = {i:[] for i in range(n)}

    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return  adj_list

adj_list = build_adj_list(n,edges)


def dfs(adj_list):
    if not adj_list:
        return
    #key difference between tree and graph
    visited = set()

    def dfs_helper(node):
        #base case to stop revisiting same nodes
        if node is visited:
            return None
        #*******important***********
        visited.add(node)

        # just like tree instead of left and right explore all nodes connected
        for neighbor in adj_list[node]:
            dfs_helper(neighbor)
        return
    dfs_helper(adj_list[0])





def validTree(n,edges):
    adj_list = build_adj_list(n, edges)

    visited =[False] * n

    def hasCycle(adj_list,node,visited,parent):
        visited[node] = True
        for neighbor in adj_list[node]:
            if visited[neighbor] and parent!= neighbor:
                return True
            elif not visited[neighbor] and hasCycle(adj_list,neighbor,visited,node):
                return True
        return False

    if hasCycle(adj_list,0,visited,-1):
        return False


'''
DFS on a matrix is similar to DFS on an adjacency list. We still have to keep track of visited nodes, and we recursively call DFS on each neighbor of the current node.
Use a set to keep track of visited nodes. Each time you visit a node, add it to the set.
If you encounter a node that has already been visited, return immediately without making any further recursive calls.
Use a for loop to iterate over each neighbor of the current node, and recursively call dfs on each neighbor. Before visiting the neighbor, check if it is within the bounds of the grid.
'''
