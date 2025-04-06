class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = []

        for char, count in freq.items():
            heapq.heappush(max_heap(-count, char))
        
        result = []
        while len(max_heap) > 1:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            result.append(char1)
            result.append(char2)

            if count1 < -1: heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 < -1: heapq.heappush(max_heap, (count2 + 1, char2))
        
        if max_heap:
            count, char = heapq.heappop(max_heap)
            if count < -1:
                return ""
            result.append(char)
        
        return ''.join(result)