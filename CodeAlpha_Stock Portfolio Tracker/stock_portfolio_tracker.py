import os

def stock_portfolio_tracker():
    # Hardcoded dictionary defining stock prices (USD)
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 175
    }

    portfolio = {}
    
    print("Welcome to Stock Portfolio Tracker")
    print("Available Stocks & Prices ($):")
    for stock, price in stock_prices.items():
        print(f"  • {stock}: ${price}")
    print("-" * 45)

    while True:
        stock_symbol = input("\nEnter Stock Symbol to buy (or type 'done' to finish): ").strip().upper()
        
        if stock_symbol == "DONE":
            break
            
        if stock_symbol not in stock_prices:
            print(" Invalid stock symbol! Please select from the list above.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_symbol}: "))
            if quantity <= 0:
                print(" Quantity must be greater than 0.")
                continue
            
            # Add or update stock in user's portfolio
            portfolio[stock_symbol] = portfolio.get(stock_symbol, 0) + quantity
            print(f"Added {quantity} shares of {stock_symbol}.")
            
        except ValueError:
            print(" Please enter a valid integer number for quantity.")

    # Calculate Total Portfolio Value
    if not portfolio:
        print("\nNo stocks added to portfolio. Exiting.")
        return

    total_value = 0
    summary_lines = []
    
    summary_lines.append("=" * 40)
    summary_lines.append("PORTFOLIO SUMMARY REPORT")
    summary_lines.append("=" * 40)
    summary_lines.append(f"{'Stock':<10} {'Qty':<10} {'Price ($)':<12} {'Total ($)':<10}")
    summary_lines.append("-" * 40)

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        item_total = qty * price
        total_value += item_total
        summary_lines.append(f"{stock:<10} {qty:<10} ${price:<11} ${item_total:<10}")

    summary_lines.append("-" * 40)
    summary_lines.append(f"TOTAL PORTFOLIO VALUE: ${total_value}")
    summary_lines.append("=" * 40)

    # Print Summary to Console
    report_text = "\n".join(summary_lines)
    print("\n" + report_text)

    # Save to File
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write(report_text)
        
    print(f"\n Portfolio summary successfully saved to '{filename}'!")

if __name__ == "__main__":
    stock_portfolio_tracker()