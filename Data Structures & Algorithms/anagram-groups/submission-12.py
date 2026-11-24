class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        countsDict = {}
        for s in strs:
            counts = [0] * len(alphabet) 
            for c in s:       
                counts[ord(c)-ord('a')] += 1
            k = tuple(counts)
            if k in countsDict:
                countsDict[k].append(s)
            else:
                countsDict[k] = [s] 

        return list(countsDict.values())       
         