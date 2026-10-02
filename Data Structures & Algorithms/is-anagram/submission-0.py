class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for j in t:
            d[j] = d.get(j,0) - 1
        for i in d.values():
            if i!=0:
                return False
        return True

        