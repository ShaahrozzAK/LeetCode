class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    pair+=1
        return pair