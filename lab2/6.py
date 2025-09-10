sales = {"apple": 30, "banana": 50, "orange": 20}
prices = {"apple": 2, "banana": 1, "orange": 3}

def total_revenue(sales: dict, prices: dict) -> int:
    total = 0
    for product, quantity in sales.items():
        if product in prices:
            total += quantity * prices[product]
    return total

print("Total revenue:", total_revenue(sales, prices))