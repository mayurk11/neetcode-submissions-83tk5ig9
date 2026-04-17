class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
# Optimal Solution
        res = 0
        for num in nums:
            res = res ^ num

        return res        
        


# Brute Force Solution

        # hash_map = {}
        # for num in nums:
        #     hash_map[num] = hash_map.get(num,0)+1

        # for key in hash_map:
        #     if hash_map[key] == 1:
        #         return key 
        
        # for i in range(len(nums)):
        #     flag = True
        #     for j in range(len(nums)):
        #         if i !=j and nums[i] == nums[j]:
        #             flag = False
        #             break
        #     if flag:
        #         return nums[i]
        