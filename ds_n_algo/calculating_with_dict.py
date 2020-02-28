prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_prices = min(zip(prices.values(), prices.keys()))
print(min_prices)

max_prices = max(zip(prices.values(), prices.keys()))
print(max_prices)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
