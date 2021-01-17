class MyHashMap:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = []
​
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        flag = 0
        for i in range(len(self.hashMap)):
            if key == self.hashMap[i][0]:
                self.hashMap[i][1] = value
                flag = 1
                break
        if flag==0:
            self.hashMap.append([key,value])
        
​
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        flag = 0
        for i in range(len(self.hashMap)):
            if key == self.hashMap[i][0]:
                flag = 1
                return self.hashMap[i][1]
        if flag==0:
            return -1
​
        
        
​
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        for i in range(len(self.hashMap)):
            if key == self.hashMap[i][0]:
                self.hashMap[i][0]=[-1]
​
​
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
