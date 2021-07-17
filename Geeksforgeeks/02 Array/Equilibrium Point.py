# URL: https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/
# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Example 1:

# Input:
# n = 1
# A[] = {1}
# Output: 1
# Explanation: Since its the only 
# element hence its the only equilibrium 
# point. 
# Example 2:

# Input:
# n = 5
# A[] = {1,3,5,2,2}
# Output: 3
# Explanation: For second test case 
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2).
 

# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium. Return -1 if no such point exists.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if(N==1):
            return 1
        leftsum = 0
        s = sum(A)
        for i in range(N):
            s -=A[i]
            if(s==leftsum):
                return i+1
            leftsum +=A[i]
        return -1
        # Your code here


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends