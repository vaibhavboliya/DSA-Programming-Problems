# URL : https://practice.geeksforgeeks.org/problems/majority-element-1587115620/0/
# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
 

# Example 1:

# Input:
# N = 3 
# A[] = {1,2,3} 
# Output:
# -1
# Explanation:
# Since, each element in 
# {1,2,3} appears only once so there 
# is no majority element.
# Example 2:

# Input:
# N = 5 
# A[] = {3,1,3,3,2} 
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is 
# the majority element.

# Your Task:
# The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
 

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

class Solution:
    def majorityElement(self, A, N):
        freq = {}
        for X in A:
            freq[X] = freq.get(X,0)+1
        for X in freq:
            if(N//2<freq[X]):
                return X
        return -1
            
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends