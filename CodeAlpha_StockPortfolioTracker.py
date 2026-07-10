def stock_portfolio_tracker():
    # ANSI Escape Codes for text styling and colors
    CLR_TITLE = "\033[95m"    # Pink/Magenta
    CLR_HEADER = "\033[96m"   # Cyan
    CLR_MONEY = "\033[92m"    # Green
    CLR_WARN = "\033[93m"     # Yellow
    CLR_ERROR = "\033[91m"    # Red
    STYLE_BOLD = "\033[1m"
    STYLE_RESET = "\033[0m"

    # Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 400,
        "GOOG": 150,
        "AMZN": 175
    }

    user_portfolio = {}

    # Creative ASCII Art Header
    print(f"{CLR_TITLE}{STYLE_BOLD}")
    print(r"   ┌─────────────────────────────────────────┐")
    print(r"   │       📊 STOCK PORTFOLIO TRACKER 📊     │")
    print(r"   └─────────────────────────────────────────┘")
    print(f"{STYLE_RESET}")

    # Displaying available markets in a styled box
    print(f"{CLR_HEADER}{STYLE_BOLD}┌─────────────────────────────────────────┐")
    print("│      TICKER      │    CURRENT PRICE     │")
    print(f"├──────────────────┼──────────────────────┤{STYLE_RESET}")
    for stock, price in stock_prices.items():
        print(f"│     {stock:<12} │        {CLR_MONEY}${price:<13}{STYLE_RESET} │")
    print(f"{CLR_HEADER}{STYLE_BOLD}└─────────────────────────────────────────┘{STYLE_RESET}\n")

    # Interactive input loop
    while True:
        ticker = input(f"{STYLE_BOLD}👉 Enter Stock Ticker (or type 'done' to finish): {STYLE_RESET}").upper().strip()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_prices:
            print(f"{CLR_ERROR}❌ Ticker '{ticker}' not found. Please choose from the list above.{STYLE_RESET}\n")
            continue

        try:
            quantity = int(input(f"   How many shares of {CLR_HEADER}{ticker}{STYLE_RESET} do you own? "))
            if quantity <= 0:
                print(f"{CLR_WARN}⚠️ Quantity must be a positive whole number.{STYLE_RESET}\n")
                continue
        except ValueError:
            print(f"{CLR_ERROR}❌ Invalid input! Please type an integer number.{STYLE_RESET}\n")
            continue

        # Save to portfolio
        user_portfolio[ticker] = user_portfolio.get(ticker, 0) + quantity
        print(f"{CLR_MONEY}✅ Added {quantity} share(s) of {ticker}!{STYLE_RESET}\n")

    if not user_portfolio:
        print(f"\n{CLR_WARN}No data collected. Exiting program.{STYLE_RESET}")
        return

    # Visualizing the final results in an advanced dashboard table
    print("\n" + "="*53)
    print(f"{CLR_TITLE}{STYLE_BOLD}                💼 YOUR INVESTMENT DASHBOARD             {STYLE_RESET}")
    print("="*53)
    
    print(f"{CLR_HEADER}{STYLE_BOLD}┌──────────┬──────────────┬──────────────┬──────────────┐")
    print("│  TICKER  │  SHARES HELD │  UNIT PRICE  │ TOTAL VALUE  │")
    print(f"├──────────┼──────────────┼──────────────┼──────────────┤{STYLE_RESET}")
    
    total_portfolio_value = 0
    file_output_lines = []

    for stock, qty in user_portfolio.items():
        price = stock_prices[stock]
        holding_value = qty * price
        total_portfolio_value += holding_value
        
        # Format values for display (with colors)
        print(f"│  {STYLE_BOLD}{stock:<7}{STYLE_RESET} │  {qty:<12} │  ${price:<11} │  {CLR_MONEY}${holding_value:<11,}{STYLE_RESET} │")
        
        # Clean text layout format for file storage (without ANSI color garbage characters)
        file_output_lines.append(f"│  {stock:<7} │  {qty:<12} │  ${price:<11} │  ${holding_value:<11,} │")

    print(f"{CLR_HEADER}{STYLE_BOLD}├──────────┴──────────────┴──────────────┼──────────────┤{STYLE_RESET}")
    print(f"│ {STYLE_BOLD}NET WORTH VALUE:{STYLE_RESET:<23} │ {CLR_MONEY}{STYLE_BOLD}${total_portfolio_value:<12,}{STYLE_RESET} │")
    print(f"{CLR_HEADER}{STYLE_BOLD}└────────────────────────────────────────┴──────────────┘{STYLE_RESET}")

    # File export segment
    save_file = input(f"\n{STYLE_BOLD}💾 Save report to a spreadsheet-ready .txt file? (yes/no): {STYLE_RESET}").lower().strip()
    if save_file in ['yes', 'y']:
        filename = "portfolio_summary.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write("┌─────────────────────────────────────────────────────┐\n")
            file.write("│               STOCK PORTFOLIO REPORT                │\n")
            file.write("├─────────────────────────────────────────────────────┤\n")
            file.write("│  TICKER  │  SHARES HELD │  UNIT PRICE  │ TOTAL VALUE  │\n")
            file.write("├──────────┼──────────────┼──────────────┼──────────────┤\n")
            for line in file_output_lines:
                file.write(line + "\n")
            file.write("├──────────┴──────────────┴──────────────┼──────────────┤\n")
            file.write(f"│ NET WORTH VALUE:                        │ ${total_portfolio_value:<12,} │\n")
            file.write("└────────────────────────────────────────┴──────────────┘\n")
        print(f"{CLR_MONEY}✨ Success! A beautifully formatted report was saved as '{filename}'.{STYLE_RESET}")

if __name__ == "__main__":
    stock_portfolio_tracker()