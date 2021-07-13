# Given the adjacency list of a bidirectional graph. Your task is to return the adjacency list for each vertex.
# Example 1:

# Input:
# v E

# Output:
# 0-> 1-> 4
# 1-> 0-> 2-> 3-> 4
# 2-> 1-> 3
# 3-> 1-> 2-> 4
# 4-> 0-> 1-> 3
# Explanation:
# As 0,1 and 3 is connected to 4 so 4th row
# of the list containing 4 and its connected
# nodes 0,1 and 3 and we have to add those in
# sorted order and same for every row.


# Your task:
# You don’t need to read input or print anything. Your task is to complete the function printGraph() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns the list of list  contains the node itself with its connected nodes(as same as it is given in input adjacency  list).


# Expected Time Complexity: O(V + E)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ V, E ≤ 104


class Solution:

    # Function to return the adjacency list for each vertex.
    def printGraph(self, V, adj):
        print
        lis = [[] for i in range(V)]
        for i in range(len(adj)):
            lis[i].append(i)
            lis[i].extend(adj[i])
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
        obj = Solution()
        ans = obj.printGraph(V, adj)
        for i in range(len(ans)):
            for j in range(len(ans[i])-1):
                print(ans[i][j], end="-> ")
            print(ans[i][len(ans[i])-1])

# } Driver Code Ends
