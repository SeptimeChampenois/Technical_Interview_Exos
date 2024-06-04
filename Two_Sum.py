class Solution(object):
    def twoSum(self, nums, target):
        # Create a hashmap to store the numbers and their indices
        num_to_index = {}
        # Iterate over the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # Check if the complement is in the hashmap
            if complement in num_to_index:
                # If it is, return the indices of the current number and the complement
                return [num_to_index[complement], i] 
            # If it isn't, add the number and its index to the hashmap
            num_to_index[num] = i


# class Solution(object):
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
