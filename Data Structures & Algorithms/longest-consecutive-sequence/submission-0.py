class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for num in nums:
            if num-1 not in nums:
                len = 1
                while num+len in nums:
                    len += 1
                best = max(best, len)
        return best
        