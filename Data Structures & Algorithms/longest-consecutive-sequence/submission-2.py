class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_count = 0
        
        for i in range(0,n):
            num = nums[i]
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1
            max_count = max(max_count , count)
        
        return max_count
        
        
        # res = 0
        # num_set =set(nums)

        # for num in num_set:

        #     if (num-1) not in num_set:
        #         streak = 0
        #         curr = num
        #         while curr in num_set:
        #             streak +=1
        #             curr +=1
        #         res = max(res,streak)

        # return res