class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # Handle the edge case where the array is empty
            return 0

        # Pointer for the position of the last unique element
        unique_index = 0

        # Start from the second element and check for duplicates
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:  # If current element is different from the last unique element
                unique_index += 1  # Move the unique pointer
                nums[unique_index] = nums[i]  # Update the next unique position

        # The number of unique elements is unique_index + 1
        return unique_index + 1


# Example usage
solution = Solution()
nums = [1, 1, 2, 2, 3, 4]
k = solution.removeDuplicates(nums)
print("Number of unique elements: {}".format(k))  # Output: 4
print("Array after removing duplicates: {}".format(nums[:k]))  # Output: [1, 2, 3, 4]
