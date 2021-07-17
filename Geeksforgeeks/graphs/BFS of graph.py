# URL : https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1/
# Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
# Note: One can move from node u to node v only if there's an edge from u to v and find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the graph.
# Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.

# Example 1:

# Input:
# 5 5
# 1 0
# 0 2
# 2 1
# 2 3
# 3 4

# Output: 0 1 2 3 4
# Explanation:
# 0 is connected to 1 , 2 , 3.
# 2 is connected to 4.
# so starting from 0, it will go to 1 then 2
# then 3.After this 2 to 4, thus bfs will be
# 0 1 2 3 4.


# Your task:
# You don’t need to read input or print anything. Your task is to complete the function bfsOfGraph() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns  a list containing the BFS traversal of the graph starting from the 0th vertex from left to right.


# Expected Time Complexity: O(V + E)
# Expected Auxiliary Space: O(V)


# Constraints:
# 1 ≤ V, E ≤ 104


class Solution:
    def bfsOfGraph(self, V, adj):
        visited = [False]*V
        queue = []
        lis = []
        queue.append[0]
        while queue:
            x = queue.pop(0)
            if not visited[x]:
                lis.append(x)
            visited[x] = True
            for i in adj[x]:
                if visited[i] == False:
                    queue.append(i)
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
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()


# } Driver Code Ends
