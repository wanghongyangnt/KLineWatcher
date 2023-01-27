# 存储k线图数据
class KLineData:
    def __init__(self, openPrice, closePrice, maxPrice, minPrice):
        self.openPrice = openPrice
        self.closePrice = closePrice
        self.maxPrice = maxPrice
        self.minPrice = minPrice