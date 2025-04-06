class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_heap = []

        for num, count in freq.items():
            heapq.heappush(max_heap, (-count, num))

        result = []

        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
        
        return result