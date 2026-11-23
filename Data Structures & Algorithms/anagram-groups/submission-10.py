class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in words:
                words[key].append(s)
            else:
                words[key] = [s]
        return list(words.values())