class MyHashMap(object):

    def __init__(self):
        self.HashMap={}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.HashMap[key]=value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.HashMap.keys():
            return self.HashMap[key]
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.HashMap.keys():
            self.HashMap.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)