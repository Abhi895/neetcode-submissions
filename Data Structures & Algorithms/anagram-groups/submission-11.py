class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        countsDict = {}
        # for l in alphabet:
        #     aDict[l] = 
        
        for s in strs:
            counts = [0] * len(alphabet) 
            for c in s:       
                for i in range(len(alphabet)):
                    if alphabet[i] == c:
                        counts[i] += 1
            k = tuple(counts)
            if k in countsDict:
                countsDict[k].append(s)
            else:
                countsDict[k] = [s] 

        return list(countsDict.values())       
         