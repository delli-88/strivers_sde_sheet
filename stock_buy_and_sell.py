from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    n = len(prices)
    max_profit = 0
    min_val = prices[0]
    for i in range(1,n):
        profit = prices[i]-min_val
        max_profit = max(max_profit,profit)
        min_val = min(min_val,prices[i])
    return max_profit

print(maximumProfit(prices = [7,1,5,3,6,4]))