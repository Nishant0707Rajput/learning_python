class Hashmap:

    def __init__(self, val):
        self.val = val
        self.arr = [None] * self.val

    def get_hash(self,key):
        sum_val = 0

        for i in key:
            sum_val += ord(i)
        return sum_val % self.val

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


an_obj = Hashmap(100)
print(an_obj.get_hash("your"))
an_obj["newman"] = "possible"
print(an_obj["newman"])



