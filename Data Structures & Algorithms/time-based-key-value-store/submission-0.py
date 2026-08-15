class TimeMap:

    def __init__(self):
        self.cont = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cont[timestamp] = {key: value}

    def get(self, key: str, timestamp: int) -> str:
        if self.cont.get(timestamp, None) is not None:
            temp = self.cont[timestamp]
            if key in temp:
                return self.cont[timestamp][key]
        
        for i in range(timestamp-1, -1, -1):
            if self.cont.get(i, None) is not None:
                temp = self.cont[i]
                if key in temp:
                    return temp[key]
            
        return ""