class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}


        for char in strs:
            if "".join(sorted(char)) not in anagramDict:
                anagramDict["".join(sorted(char))] = [char]
            else:
                anagramDict["".join(sorted(char))].append(char)

        return [c for c in anagramDict.values()]


            