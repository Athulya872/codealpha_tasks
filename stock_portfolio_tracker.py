# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 170
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    # Get stock name from user
    stock = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    # Check if stock exists
    if stock not in stock_prices:
        print("Stock not found! Please enter a valid stock name.")
        continue

    # Get quantity
    quantity = int(input("Enter quantity: "))

    # Calculate investment
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock} Investment = ${investment}")

    # Ask if user wants to add another stock
    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

# Display total investment
print("\nTotal Investment Value = $", total_investment)

# Save the result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Portfolio saved to portfolio.txt")