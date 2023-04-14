# You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    down = prices[0]
    up = down
    bestSell = up - down
    for i in range(len(prices)):
        if prices[i] < down:
            down = prices[i]
            up = down
        if prices[i] > up:
            up = prices[i]
            if up - down > bestSell:
                bestSell = up - down
    return bestSell


if __name__ == '__main__':
    print(maxProfit([7,6,4,3,1]))