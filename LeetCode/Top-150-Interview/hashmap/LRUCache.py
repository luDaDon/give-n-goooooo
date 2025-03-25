from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums_map = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.nums_map:
            return -1
            
        self.nums_map.move_to_end(key)

        return self.nums_map.get(key)
        

    def put(self, key: int, value: int) -> None:
        if key in self.nums_map:
            self.nums_map.move_to_end(key)
        self.nums_map[key] = value
        
        if len(self.nums_map) > self.capacity:
            self.nums_map.popitem(False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)