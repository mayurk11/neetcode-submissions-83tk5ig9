class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1 
                elif three_sum < 0:
                    l += 1 
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res







    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = set()
    #     nums.sort()
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     tmp = [nums[i], nums[j], nums[k]]
    #                     res.add(tuple(tmp))
    #     return [list(i) for i in res]