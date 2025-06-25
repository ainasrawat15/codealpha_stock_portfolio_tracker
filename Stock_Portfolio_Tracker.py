# Stock Portfolio Tracker using dictionary and user input

def portfolio_tracker():
    portfolio = {}  # Dictionary to store stock data
    print("\n📈 Welcome to the Stock Portfolio Tracker!")
    print("Enter your stocks. Type 'done' to finish.\n")

    while True:
        ticker = input("Enter stock ticker (e.g., AAPL): ").upper().strip()
        if ticker == "DONE":
            break

        try:
            shares = int(input(f"Enter number of shares for {ticker}: "))
            buy_price = float(input(f"Enter buy price for {ticker} ($): "))
        except ValueError:
            print("⚠️ Please enter valid numbers for shares and price.\n")
            continue

        # Store data in the dictionary
        portfolio[ticker] = {"shares": shares, "buy_price": buy_price}

    # Display portfolio summary
    print("\n📊 Portfolio Summary:\n")
    print(f"{'Ticker':<10}{'Shares':<10}{'Buy Price':<15}{'Invested ($)':<15}")
    total_investment = 0

    for ticker, data in portfolio.items():
        shares = data["shares"]
        buy_price = data["buy_price"]
        invested = shares * buy_price
        total_investment += invested
        print(f"{ticker:<10}{shares:<10}{'$'+str(buy_price):<15}{'$'+str(round(invested, 2)):<15}")

    print("\n💰 Total Investment: $", round(total_investment, 2))


portfolio_tracker()
