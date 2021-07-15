# URL : https://practice.geeksforgeeks.org/problems/eulerian-path-in-an-undirected-graph5052/1
# Given an adjacency matrix representation of an unweighted undirected graph named graph, which has N vertices. You have to find out if there is an eulerian path present in the graph or not.
# Note: The graph consists of a single component

# Example 1:

# Input: N = 5
# graph = {{0, 1, 0, 0, 1},
#          {1, 0, 1, 1, 0},
#          {0, 1, 0, 1, 0},
#          {0, 1, 1, 0, 0},
#          {1, 0, 0, 0, 0}}
# Output: 1
# Explaination: There is an eulerian path.
# The path is 5->1->2->4->3->2.
# Your Task:
# You do not need to read input or print anything. Your task is to complete the function eulerPath() which takes N and graph as input parameters and returns 1 if there is an eulerian path. Otherwise returns 0.

# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(N2)

# Constraints:
# 1 ≤ N ≤ 50


class Solution:
    def eulerPath(self, n, graph):

        numofadj = []

        for i in range(n):
            numofadj.append(sum(graph[i]))

        startpoint, numofodd = 0, 0
        for i in range(n - 1, -1, -1):
            if (numofadj[i] % 2 == 1):
                numofodd += 1
                startpoint = i

        if (numofodd > 2):
            return 0

    # If there is a path find the path
    # Initialize empty stack and path
    # take the starting current as discussed
        stack = []
        path = []
        cur = startpoint

    # Loop will run until there is element in the
    # stack or current edge has some neighbour.
        while (len(stack) > 0 or sum(graph[cur]) != 0):

            # If current node has not any neighbour
            # add it to path and pop stack set new
            # current to the popped element
            if (sum(graph[cur]) == 0):
                path.append(cur)
                cur = stack[-1]
                del stack[-1]

        # If the current vertex has at least one
        # neighbour add the current vertex to stack,
        # remove the edge between them and set the
        # current to its neighbour.
            else:
                for i in range(n):
                    if (graph[cur][i] == 1):
                        stack.append(cur)
                        graph[cur][i] = 0
                        graph[i][cur] = 0
                        cur = i
                        break
        return 1

        # code here

# {
#  Driver Code Starts
# Initial Template for Python3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        graph = []
        for i in range(N):
            graph.append(list(map(int, input().strip().split())))

        ob = Solution()
        print(ob.eulerPath(N, graph))
# } Driver Code Ends
