class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
        freq = [k for k in counts.keys()]
        freq.reverse()
        return freq[:k]
