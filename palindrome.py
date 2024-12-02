class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert the number to a string and check if it equals its reverse
        x = str(x)  # Convert the integer to a string
        return x == x[::-1]

# Example usage
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
