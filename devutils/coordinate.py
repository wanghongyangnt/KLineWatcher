class Coordinate(object):
    # 初始化坐标系，设置实际显示时所占据的像素宽高
    def __init__(self, width, height):
        self.pixel_width = width    # 实际显示像素坐标系宽度，窗口左上角为坐标系零点
        self.pixel_height = height  # 实际显示像素坐标系高度
        self.begin_date = 0         # 开始日期，x轴起点
        self.end_date = 0           # 终止日期，
        self.value_low = 0          # 最低值
        self.value_high = 0         # 最高值
        self.x_scale = 1            # x轴缩放因子
        self.y_scale = 1            # y轴缩放因子

    # 更新坐标系，通过要显示的不同数据，更新坐标系中其余参数，如开始日期等
    def update(self, values):   # value为要显示的数据，根据日期进行切片
        x_max = y_max = 10000   # 记录全部数据的最大值
        x_min = y_min = 0       # 记录最小值
        # 根据date确定x轴最大值和最小值，根据high确定y轴最大值，根据low确定y轴最小值
        for date, high, open, close, low in values:
            x_max = max(x_max, date)
            y_max = max(y_max, high)
            x_min = min(x_min, date)
            y_min = min(y_min, low)
        self.begin_date = x_min
        self.end_date = x_max
        self.value_low = y_min
        self.value_high = y_max
        # 根据规划化方法对数据进行
        self.x_scale = self.pixel_width / (self.end_date - self.begin_date)
        self.y_scale = self.pixel_height / (self.value_high - self.value_low)

    def transform(self, values):
        self.update(values)
        coord_values = []
        for date, high, open, close, low in values:
            temp_date = (date - self.begin_date) * self.x_scale
            temp_high = (high - self.value_low) * self.y_scale
            temp_open = (open - self.value_low) * self.y_scale
            temp_close = (close - self.value_low) * self.y_scale
            temp_low = (low - self.value_low) * self.y_scale
            coord_values.append([temp_date, temp_high, temp_open, temp_close, temp_low])
        return coord_values


class Kline(object):
    class Item(object):
        def __init__(self, date, high, open, close, low):
            self.date = date
            self.high = high
            self.open = open
            self.close = close
            self.low = low

    def __init__(self):
        self.data = []
        self.draw_data = []


if __name__ == "__main__":
    kline = Kline()
    coord = Coordinate(100, 100)
    kline.draw_data = coord.transform(kline.data[1:10])