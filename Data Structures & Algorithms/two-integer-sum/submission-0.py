class Solution:
    def twoSum(self, nums, target):
        # Create an empty Hash Map to store {number: index}
        num_map = {}
        
        # Enumerate gives us both the index (i) and the number (num)
        for i, num in enumerate(nums):
            balance = target - num
            
            # Check if the balance is ALREADY in the map
            if balance in num_map:
                # Pair found! Return the saved index and the current index
                return [num_map[balance], i]
                
            # If not found, save the current number and its index for later
            num_map[num] = i