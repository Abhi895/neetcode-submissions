class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}


        for word in strs:
            key = "".join(sorted(word))
            if key  not in anagramDict:
                anagramDict[key] = [word]
            else:
                anagramDict[key].append(word)

        return list(anagramDict.values())


            