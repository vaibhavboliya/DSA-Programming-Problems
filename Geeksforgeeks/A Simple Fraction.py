# URL : https://practice.geeksforgeeks.org/problems/a-simple-fraction0921/0/

# Given a fraction. Convert it into a decimal.
# If the fractional part is repeating, enclose the repeating part in parentheses.


# Example 1:

# Input: numerator = 1, denominator = 3
# Output: "0.(3)"
# Explanation: 1/3 = 0.3333... So here 3 is
# recurring.
# Example 2:

# Input: numerator = 5, denominator = 2
# Output: "2.5"
# Explanation: 5/2 = 2.5


# Your Task:
# You don't need to read or print anyhting. Your task is to complete the function fractionToDecimal() which takes numerator and denominator as input parameter and returns its decimal form in string format.


# Expected Time Compelxity: O(k) where k is constant.
# Expected Space Complexity: O(k)


# Constraints:
# 1 ≤ numerator, denominator ≤ 2000

class Solution:
	def fractionToDecimal(self, numerator, denominator):
		no = str(numerator//denominator)+'.'
		remainder = numerator % denominator
		if remainder == 0:
		    return numerator//denominator
		dp = {}

		while(remainder != 0 and remainder not in dp):
		    dp[remainder] = len(no)
		    remainder = remainder*10
		    rno = remainder//denominator
		    remainder = remainder % denominator
		    no += str(rno)
        if remainder==0:
            return no
        else:
            return(no[:dp[remainder]]+'('+no[dp[remainder]:]+')')
	       
		# Code here

# { 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
# } Driver Code Ends
