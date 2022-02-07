from ast import parse
import backtrader as bt
import pandas as pd
import argparse
from strategies import TestStrategy

def getdata(csvname):

    return bt.feeds.YahooFinanceCSVData(dataname=csvname)

def main(csvname, strategy=None, startingcash=10000, commission=None, sizertype='Percent', sizeramt=0.95):
    data = getdata(csvname)
    cerebro = bt.Cerebro()
    cerebro.broker.setcommission(commission=commission) if commission else None
    cerebro.broker.setcash(startingcash)
    
    if data is not None:
        cerebro.adddata(data)
        cerebro.addsizer(bt.sizers.PercentSizer, percents=sizeramt) if sizeramt and sizertype == 'Percent' else cerebro.addsizer(bt.sizers.FixedSize, stake=sizeramt)
    
    cerebro.addstrategy(strategy) if strategy is not None else None
    
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()

if __name__ == '__main__':
   main('AAPL.csv', TestStrategy)
   
