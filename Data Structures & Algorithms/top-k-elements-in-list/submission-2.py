class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        list1 = []
        for num, cnt in count.items():  #count.items to get both key and value
            list1.append([cnt, num])       # adds liek this ##
                                                          ##
                                                          ##
        
        list1.sort(reverse=True)

        j = 0
        result = []
        while len(result) < k:
            result.append(list1[j][1])
            j+=1
        
        return result

        

