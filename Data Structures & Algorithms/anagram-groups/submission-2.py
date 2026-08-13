class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        map1 = {}
        for i in strs:
            key = "".join(sorted(i))
            if not key in map1:
                map1[key] = []
            map1[key].append(i)
        return list(map1.values()) #returns list of values