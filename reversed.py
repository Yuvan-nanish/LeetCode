class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle the sign of the number
        sign = -1 if x < 0 else 1
        
        # Reverse the absolute value and apply the sign
        reversed_x = int(str(abs(x))[::-1]) * sign
        
        # Handle overflow for 32-bit integers
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x

# Example usage
solution = Solution()
print(solution.reverse(123))    # Output: 321
print(solution.reverse(-123))   # Output: -321
print(solution.reverse(120))    # Output: 21
print(solution.reverse(1534236469))  # Output: 0 (due to overflow)
