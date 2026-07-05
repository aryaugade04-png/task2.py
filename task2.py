# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

total_value = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock)

n = int(input("\nEnter the number of different stocks you own: "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock_name] * quantity
        total_value += value
    else:
        print("Stock not found!")

print("\nTotal Investment Value = ₹", total_value)

# Save result in a text file
with open("portfolio_summary.txt", "w") as file:
    file.write(f"Total Investment Value = ₹{total_value}")

print("Portfolio summary saved as portfolio_summary.txt")