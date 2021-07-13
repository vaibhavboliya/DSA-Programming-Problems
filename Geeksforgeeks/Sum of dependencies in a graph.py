# Given a directed graph with V nodes and E edges. If there is an edge from u to v then u depends on v. Find out the sum of dependencies for every node. Duplicate edges should be counted as separate edges.

# Example 1:

# Input:
# V=4
# E=4
# Edges={ {0,2},{0,3},{1,3},{2,3} }
# Output:
# 4
# Explanation:
# For the graph in diagram, A depends
# on C and D i.e. 2, B depends on D i.e.
# 1, C depends on D i.e. 1
# and D depends on none.
# Hence answer -> 0 + 1 + 1 + 2 = 4
# Example 2:

# Input:
# V=4
# E=3
# Edges={ {0,3},{0,2},{0,1} }
# Output:
# 3
# Explanation:
# The sum of dependencies=3+0+0+0=3.

# Expected Time Complexity:O(V)
# Expected Auxillary Space:O(1)


# Constraints:
# 1<=V,E<=150

# 0<= Edges[i][0],Edges[i][1] <= V-1


import math


class Solution:
    def sumOfDependencies(self, adj, V):
        count = 0
        for i in adj:
            count += len(i)
        return count


# Driver Code

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        a = [[] for i in range(N)]
        s = list(map(int, input().strip().split()))
        for i in range(0, 2*M, 2):
            x = s[i]
            y = s[i+1]
            a[x].append(y)
        ob = Solution()
        print(ob.sumOfDependencies(a, N))
