#🔹 PART 1: 

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")

#🔹 PART 2: User Input Loop for Adding Stocks

print("\nEnter stock details (type 'done' to finish):")

# Input loop
while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than zero.\n")
            continue
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    print("✅ Stock added successfully!\n")

    #🔹 PART 3: Portfolio Calculation & Display

# Calculate total investment
print("\n📊 Portfolio Summary:")
print("----------------------")

for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock} | Quantity: {qty} | Value: ₹{investment}")

print("----------------------")
print(f"💰 Total Investment Value: ₹{total_investment}")

#LAST LINE

print("\n✅ Program completed. Thank you!")


