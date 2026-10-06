class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in strs:
            result = result + str(len(i)) + '#' + i
        return result

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            results.append(s[j+1: j+1+l])
            i = j+1+l
        return results
            
