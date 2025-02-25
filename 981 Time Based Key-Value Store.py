'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''

from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.object_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.object_map:
            self.object_map[key] = SortedDict() 
        self.object_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.object_map:
            if timestamp in self.object_map[key]:
                return self.object_map[key][timestamp]
            
            candidate = self.object_map[key].bisect_left(timestamp)
            if candidate > 0:
                candidate -= 1
                return self.object_map[key].values()[candidate]
        
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
