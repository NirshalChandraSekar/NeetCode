class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key, value, timestamp):
        if key not in self.dict:
            self.dict[key] = [[value,timestamp]]
        else:
            self.dict[key].append([value,timestamp])

    def get(self, key, timestamp):
        if key not in self.dict:
            return ""
        
        lower = 0
        upper = len(self.dict[key])-1

        while lower<=upper:
            mid = lower + (upper - lower) // 2

            if timestamp == self.dict[key][mid][1]:
                return self.dict[key][mid][0]

            elif timestamp < self.dict[key][mid][1]:
                upper = mid-1

            else:
                lower = mid+1
        
        if upper>=0:
            return self.dict[key][upper][0]

        return ""


if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo","bar",1)
    print(obj.get("foo",1))
    print(obj.get("foo",3))
    obj.set("foo","bar2",4)
    print(obj.get("foo",4))
    print(obj.get("foo",5))
    obj.set("foo","bar3",5)
    print(obj.get("foo",5))
    print(obj.get("foo",6))