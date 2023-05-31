class UndergroundSystem:
    checkin = dict()
    times = collections.defaultdict(list)

    def __init__(self):
        pass

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ti, start = self.checkin[id]
        del self.checkin[id]
        self.times[start + ' ' + stationName].append(t - ti)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return statistics.mean(self.times[startStation + ' ' + endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)