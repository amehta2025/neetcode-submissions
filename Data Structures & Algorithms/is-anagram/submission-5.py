class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # OnLogn solution: return sorted(s) == sorted(t)
        if (len(s) != len(t)):
            return False
        mapS, mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1  # does key exist? if not make it zero, then update to 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1
        
        return mapS == mapT