# Geek is hosting a contest and N students are interested in it. But some of them are friends. Geek wants to make two teams such that no two friends are on the same team.  The task is to check is it possible for the geek two make two teams or not

# Note:
# 1. All the students are numbered from 1 to N.
# 2. If A is a friend of B and B is a friend of C, that doesn't mean that A is friend of C

# Input:
# 1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# 2. The first line of each test case contains two space_separated integers N and M.
# 3. Next M lines contain two space-separated integers u and v, represents u is a friend of v


# Output: For each test case, print the "yes" if possible, otherwise print "no" (without quotes).
# Constraints:
# 1. 1 <= T <= 100
# 2. 2 <= N <= 50
# 3. 0 <= M <= min(1000, N*(N-1)/2)


# Example:
# Input:
# 2
# 4 2
# 1 2
# 3 4
# 3 3
# 1 2
# 2 3
# 3 1

# Output:
# yes
# no


def func(adj, visit, i):
    visit[i] = 0
    q = []
    q.append([i, 0])
    while(q):
        n, c = q.pop(0)
        for node in adj[n]:
            if(visit[node] == -1):
                visit[node] = not c
                q.append([node, visit[node]])
            else:
                if(visit[n] == visit[node]):
                    return False
    return True


def isPossible(adj, v):
    visit = [-1]*v
    for i in range(v):
        if(visit[i] == -1):
            if not func(adj, visit, i):
                return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        adj = [[] for i in range(n)]
        for i in range(m):
            u, v = map(int, input().split())
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        if(isPossible(adj, n)):
            print('yes')
        else:
            print('no')
