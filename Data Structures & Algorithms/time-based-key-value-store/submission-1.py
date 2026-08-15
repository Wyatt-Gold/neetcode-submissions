class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        # [[value, timestamp],[value, timestamp]]
        value = self.timeMap.get(key, [])
        l = 0
        r = len(value) - 1
        while l <= r:
            m = l + (r - l) // 2
            if value[m][1] <= timestamp:
                result = value[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
