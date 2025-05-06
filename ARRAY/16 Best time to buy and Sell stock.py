#two pointer
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

#dynamic programming
def maxProfit(prices):
    if not prices:
        return 0
    n = len(prices)
    min_price = [0] * n
    profit = [0] * n
    min_price[0] = prices[0]
    for i in range(1, n):
        min_price[i] = min(min_price[i-1], prices[i])
        profit[i] = max(profit[i-1], prices[i] - min_price[i])
    return profit[-1]

#sliding window
def maxProfit(prices):
    if not prices:
        return 0
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
