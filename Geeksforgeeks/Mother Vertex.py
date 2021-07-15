# URL: https://practice.geeksforgeeks.org/problems/mother-vertex/0
# Given a Directed Graph, find a Mother Vertex in the Graph (if present).
# A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.
# INput:
# 1->0
# 0->2,3
# 2->1
# 3->4
# Output: 0
# Explanation: According to the given edges, all
# nodes can be reaced from nodes from 0, 1 and 2.
# But, since 0 is minimum among 0,1 and 3, so 0
# is the output.
# Your Task:
# You don't need to read or print anything. Your task is to complete the function findMotherVertex() which takes V denoting the number of vertices and adjacency list as imput parameter and returns the verticex from through which we can traverse all other vertices of the graph. If there is more than one possible nodes then returns the node with minimum value.If not possible returns -1.


# Expected Time Complexity: O(V + E)
# Expected Space Compelxity: O(V)


import sys


class Solution:

    # Function to find a Mother Vertex in the Graph.
    def findMotherVertex(self, V, adj):
        def dfs(v, visited, adj):
            visited[v] = True
            for i in adj[v]:
                if(visited[i] == False):
                    dfs(i, visited, adj)
        visited = [False]*V
        v = 0
        for i in range(V):
            if(visited[i] == False):
                dfs(i, visited, adj)
                v = i
        visited = [False]*V
        dfs(v, visited, adj)
        for i in range(V):
            if(visited[i] == False):
                return -1
        return v


# {
#  Driver Code Starts
# Initial Template for Python 3


sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.findMotherVertex(V, adj)
        print(ans)
# } Driver Code Ends
