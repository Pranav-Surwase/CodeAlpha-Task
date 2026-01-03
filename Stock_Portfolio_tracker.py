# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = []

print("Available Stocks:", stock_prices.keys())

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name not in stock_prices:
        print("Stock not available!")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment
    
    portfolio.append((stock_name, quantity, investment))
    print(f"Added {stock_name}: ₹{investment}")

print("\n--- Portfolio Summary ---")
for stock in portfolio:
    print(f"{stock[0]} | Quantity: {stock[1]} | Value: ₹{stock[2]}")

print("Total Investment Value: ₹", total_investment)

# Optional: Save to file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock in portfolio:
            file.write(f"{stock[0]} - Qty: {stock[1]} - Value: ₹{stock[2]}\n")
        file.write(f"Total Investment: ₹{total_investment}")
    
    print("Portfolio saved to portfolio.txt")
