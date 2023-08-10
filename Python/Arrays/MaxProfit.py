# Suppose you are given a list of integers, prices,
# that represent the price of Google's stock over time.
# prices[i] is the price of the stock on day i.
# You must buy the stock once and then later sell it.
# You are not allowed to sell before you buy. Write a function that returns an integer,
# which is the maximum profit you can make from buying the stock and
# then later selling it. If the list is empty, return 0

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices = [7, , 5, 3, 6, 4]
profit = max_profit(prices)
print(profit)