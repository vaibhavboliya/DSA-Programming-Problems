# Given a connected undirected graph. Perform a Depth First Traversal of the graph.
# Note: Use recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.
# Input:
# V E
# Output: 0 1 2 4 3
# Explanation:
# 0 is connected to 1, 2, 4.
# 1 is connected to 0.
# 2 is connected to 0.
# 3 is connected to 0.
# 4 is connected to 0, 3.
# so starting from 0, it will go to 1 then 2
# then 4, and then from 4 to 3.
# Thus dfs will be 0 1 2 4 3.

# Your task:
# You don’t need to read input or print anything.
#  Your task is to complete the function dfsOfGraph() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns  a list containing the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.


# Expected Time Complexity: O(V + E)
# Expected Auxiliary Space: O(V)


# Constraints:
# 1 ≤ V, E ≤ 104


class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        lis = []

        def dfs(v, lis):
            lis.append(v)
            for i in adj[v]:
                if i not in lis:
                    dfs(i, lis)
        lis = []
        dfs(0, lis)
        return lis


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
    ob = Solution()
    ans = ob.dfsOfGraph(V, adj)
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()


# } Driver Code Ends
