class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = 0
        self.tail = 0
        self.size = 0
    def get(self, key):
        if key in self.dict:
            self.dict[key] = self.head
            self.head += 1
            return self.dict[key]


    def set(self, key, value):
        if key in self.dict:
            self.dict[key].value = value
        else:
            self.dict[key] = value
            self.head += 1