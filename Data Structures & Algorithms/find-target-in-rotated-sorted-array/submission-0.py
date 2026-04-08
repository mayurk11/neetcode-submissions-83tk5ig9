class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        result = -1

        for i in range(0,n):
            if nums[i] == target:
                result = i

        return result