# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOG": 140
}

portfolio_value = 0
summary = []

print("Available stocks:", ", ".join(stock_prices.keys()))

# Get user input
while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock_name == 'DONE':
        break
        
    if stock_name not in stock_prices:
        print("Stock not found. Please choose from the available list.")
        continue
        
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        # Basic arithmetic 
        value = quantity * stock_prices[stock_name]
        portfolio_value += value
        
        # Save record for the summary
        record = f"{stock_name}: {quantity} shares = ${value}"
        summary.append(record)
        print(f"Added! Current Total: ${portfolio_value}")
        
    except ValueError:
        print("Please enter a valid number for the quantity.")

# Display final total
print("\n--- Portfolio Summary ---")
for item in summary:
    print(item)
print(f"Total Investment Value: ${portfolio_value}")

# Optional: Save to file
save_option = input("\nWould you like to save this summary to a text file? (y/n): ").lower()
if save_option == 'y':
    with open("/tmp/portfolio.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for item in summary:
            file.write(item + "\n")
        file.write(f"\nTotal Investment Value: ${portfolio_value}\n")
    print("Successfully saved to portfolio.txt")