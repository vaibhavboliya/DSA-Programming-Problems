# URL: https://practice.geeksforgeeks.org/problems/count-the-paths4332/1


# Given a directed acyclic graph(DAG) with n nodes labeled from 0 to n-1.
#  Given edges, s and d ,count the number of ways to reach from s to d.
# There is a directed Edge from vertex edges[i][0] to the vertex edges[i][1].


# Example:

# Input: edges = {{0,1},{0,3},{1,2},{3,2}},
# n = 4, s = 0, d = 2
# Output: 2
# Explanation: There are two ways to reach at
# 2 from 0. These are-
# 1. 0->1->2
# 2. 0->3->2


# Your Task:
# You don't need to read or print anything. Your task is to complete the function possible_paths()
# which takes edges, n, s and d as input parameter and returns the number of ways to reach from s to d.


# Expected Time Compelxity: O(2^n)
# Expected Space Complexity: O(n+e)

# where e is the number of edges in the graph.


from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def pathUtil(self, s, d, visited, path):
        visited[s] = True
        path.append(s)
        if s == d:
            self.count += 1
        else:
            for i in self.graph[s]:
                if visited[i] == False:
                    self.pathUtil(i, d, visited, path)
        path.pop()
        visited[s] = False

    def possible_paths(self, edges, n, s, d):
        for i in edges:
            u, v = i
            self.addEdge(u, v)

        visited = [False]*n
        path = []
        self.pathUtil(s, d, visited, path)
        return self.count

        # Code here

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m, s, d = input().split()
        n = int(n)
        m = int(m)
        s = int(s)
        d = int(d)
        edges = []
        for _ in range(m):
            x, y = input().split()
            x = int(x)
            y = int(y)
            edges.append([x, y])
        obj = Solution()
        ans = obj.possible_paths(edges, n, s, d)
        print(ans)


# } Driver Code Ends
