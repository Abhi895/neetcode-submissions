class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        freq = sorted(counts, key=counts.get, reverse=True)
        return freq[:k]
