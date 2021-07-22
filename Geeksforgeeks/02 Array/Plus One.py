# URL:https://practice.geeksforgeeks.org/problems/plus-one/0/
# Given a non-negative number represented as a list of digits, add 1 to the number (increment the number represented by the digits). The digits are stored such that the most significant digit is first element of array.
 

# Example 1:

# Input: 
# N = 3
# arr[] = {1, 2, 4}
# Output: 
# 1 2 5
# Explanation:
# 124+1 = 125, and so the Output
# Example 2:

# Input: 
# N = 3
# arr[] = {9,9,9}
# Output: 
# 1 0 0 0
# Explanation:
# 999+1 = 1000, and so the output

# Your Task:
# You don't need to read input or print anything. You only need to complete the function increment() that takes an integer N, and an array arr of size N as input and returns a list of integers denoting the new number which we get after adding one to the number denoted by the array arr.


# Expected Time Complexity:  O(N)
# Expected Auxilliary Space: O(1)


class Solution:
    def increment(self, arr, N):
        carry  = 1
        for i in range(len(arr)-1,-1,-1):
            x = arr[i]
            arr[i] = (arr[i]+carry)%10
            carry = (x+carry)//10
        if carry:
            arr.insert(0,1)
        return arr
            
        
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends