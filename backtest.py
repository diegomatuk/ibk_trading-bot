import backtrader as bt
from datetime import datetime
from strategies.GoldenCross import GoldenCross

cerebro = bt.Cerebro()
cerebro.broker.set_cash(10000)

data = bt.feeds.YahooFinanceData(dataname='SPY', fromdate=datetime(2000, 1, 1),
                                  todate=datetime(2020, 12, 31))

cerebro.adddata(data)
cerebro.addstrategy(GoldenCross)


print(cerebro.broker.getvalue())

cerebro.run()

print(cerebro.broker.getvalue())

cerebro.plot()