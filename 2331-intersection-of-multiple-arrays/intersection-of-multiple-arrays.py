class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Validate input
        if not isinstance(nums, list) or not all(isinstance(lst, list) for lst in nums):
            raise ValueError("Input must be a list of lists of integers.")
    
        if not nums:  # Empty input
            return []

        # Convert first list to a set
        common = set(nums[0])

        # Intersect with remaining lists
        for lst in nums[1:]:
            common &= set(lst)  # set intersection
            
        # Return sorted result for consistency
        return sorted(common)