class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        counts = {ke: v for ke, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
        freq = [x for x in counts.keys()]
        return freq[:k]
