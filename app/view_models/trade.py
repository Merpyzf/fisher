"""
@version: 1.0.0
@author: wangke
@time: 2018/10/13 3:14 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""

class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        # 如果需要处理一组数据时，最好现针对单个数据进行处理
        # for good in goods:
        #     self.trades.append(self.__map_to_trade(good))
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime
        else:
            time = '未知'

        return dict(
            name=single.user.nickname,
            id=single.id,
            time = time
        )