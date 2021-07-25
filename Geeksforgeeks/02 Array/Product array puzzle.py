# URL: https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/0/

# Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

 

# Example 1:

# Input:
# n = 5
# nums[] = {10, 3, 5, 6, 2}
# Output:
# 180 600 360 300 900
# Explanation: 
# For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.
# Example 2:

# Input:
# n = 2
# nums[] = {12,0}
# Output:
# 0 12

# Your Task:
# You do not have to read input. Your task is to complete the function productExceptSelf() that takes array nums[] and n as input parameters and returns a list of n integers denoting the product array P. If the array has only one element the returned list should should contains one value i.e {1}
# Note: Try to solve this problem without using the division operation.
 

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)
 

# Constraints:
# 1 <= n <= 1000
# 0 <= numsi <= 200
# Array may contain duplicates.


# USING DIVIDE 


# class Solution:
    # def productExceptSelf(self, nums, n):
    #     finalprod = 1
    #     zerocount = 0
    #     res =[None]*n
    #     for num in nums:
    #         if num!=0:
    #             finalprod = finalprod *num
    #         else:
    #             zerocount+=1
    #     for i in range(len(nums)):
    #         if(zerocount>1):
    #             res[i] =0
    #         elif(zerocount==0):
    #             res[i] = finalprod//nums[i]
    #         elif(zerocount==1):
    #             if(nums[i]==0):
    #                 res[i]=finalprod
    #             else:
    #                 res[i]=0
    #     return res

# WIthout dividing


class Solution:
        def productExceptSelf(self, arr, n):
        # Base case
            if n == 1:
            #print(0)
                return [1]
    
            i, temp = 1, 1
    
        # Allocate memory for the product array
            prod = [1 for i in range(n)]
    
        # Initialize the product array as 1
    
        # In this loop, temp variable contains product of
        # elements on left side excluding arr[i]
            for i in range(n):
                prod[i] = temp
                temp *= arr[i]
    
            # Initialize temp to 1 for product on right side
            temp = 1
    
        # In this loop, temp variable contains product of
        # elements on right side excluding arr[i]
            for i in range(n - 1, -1, -1):
                prod[i] *= temp
                temp *= arr[i]
    
            # Print the constructed prod array
        # for i in range(n):
        #     print(prod[i], end=" ")
    
            return prod

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends

