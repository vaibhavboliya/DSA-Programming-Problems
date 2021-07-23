# URL: https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1/
# Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.

# Example 1:

# Input:
# N = 6
# arr[] = {1,2,3,4,5,6}
# Output: 6 1 5 2 4 3
# Explanation: Max element = 6, min = 1, 
# second max = 5, second min = 2, and 
# so on... Modified array is : 6 1 5 2 4 3.
# Example 2:

# Input:
# N = 11
# arr[]={10,20,30,40,50,60,70,80,90,100,110}
# Output:110 10 100 20 90 30 80 40 70 50 60
# Explanation: Max element = 110, min = 10, 
# second max = 100, second min = 20, and 
# so on... Modified array is : 
# 110 10 100 20 90 30 80 40 70 50 60.
# Your Task:
# The task is to complete the function rearrange() which rearranges elements as explained above. Printing of the modified array will be handled by driver code.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= N <= 107
# 1 <= arr[i] <= 107

class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.

    def rearrange(self,arr, n): 
        maxval = arr[-1]+1
        mincount = 0
        maxcount = -1
        for i in range(n):
            if(i%2==0):
                arr[i] = arr[i]+(arr[maxcount]%maxval)*maxval
                maxcount-=1
            elif(i%2!=0):
                arr[i]=arr[i]+(arr[mincount]%maxval)*maxval
                mincount +=1
        for i,n in enumerate(arr):
            arr[i] = n//maxval     
            
        ##Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends