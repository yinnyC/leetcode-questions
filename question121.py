
def maxProfit(prices):
    # Find the min_buy_price
    # Then Find the max_sell_price
    min_buy_price = max(prices)
    maxProfit = 0
    for price in prices:
        if price < min_buy_price:
            min_buy_price = price
        elif price - min_buy_price > maxProfit:
            maxProfit = price - min_buy_price
    return maxProfit


arr = [1, 2, 3]
print(arr[:-1])
print(maxProfit([1, 2]))
