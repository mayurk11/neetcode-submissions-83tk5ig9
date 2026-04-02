class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        
        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res


        # total = 0
        # max_sum = float('-inf')

        # for i in range(len(nums)):
        #     total +=nums[i]
        #     max_sum = max(max_sum, total)
        #     if total < 0:
        #         total = 0
        # return max_sum