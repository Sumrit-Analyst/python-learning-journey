# Project: Trade Readiness Checker
# Goal: Ensure financial and mental discipline before trading.

# Get user inputs and convert to appropriate data types
account_balance = float(input("Enter your account balance: $"))
is_disciplined = str(input("Have you followed your daily routine? (yes/no): "))

# Risk constant (1% risk per trade)
risk_per_trade = 0.01

# Logic to verify trading requirements
if account_balance < 1000:
    print("Balance too low for MNQ. Focus on paper trading today.")
elif is_disciplined.lower() != "yes":
    print("Mental state check failed. Step away from the screens.")
else:
    # Calculate dollar risk if both conditions are met
    risk_amount = account_balance*risk_per_trade
    print(f"Trade Approved. Your risk for this setup is: ${risk_amount}")
