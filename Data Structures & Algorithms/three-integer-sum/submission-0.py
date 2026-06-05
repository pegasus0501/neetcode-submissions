class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Optimization: If the lowest number is positive, we can never sum to 0
            if a > 0:
                break
            
            # Prevent duplicate triplets by skipping identical anchor numbers
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Squeeze the remaining array using L and R pointers
            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = a + nums[L] + nums[R]
                
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    
                    # Prevent duplicate triplets by skipping identical L numbers
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                        
        return res