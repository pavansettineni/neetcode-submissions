class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            key = nums[i]
            d[key] = d.setdefault(key,0)+1
        items = sorted(d.items(), key = lambda x: x[1], reverse = True)
        result = []
        for num, freq in items[:k]:
            result.append(num)
        return result
        
        