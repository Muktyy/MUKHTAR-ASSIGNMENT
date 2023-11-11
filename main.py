
business_name = "Yusuf & Sons"
principal = float(input("Enter the initial principal amount: "))
rate = float(input("Enter the interest rate (as a decimal): "))
time = int(input("Enter the number of time periods elapsed: "))
compound_periods = int(input("Enter the number of times interest is compounded per time period: "))

# Calculate simple interest
simple_interest = principal * (1 + rate * time)

# Calculate compound interest
compound_interest = principal * (1 + rate/compound_periods)**(compound_periods*time)

# Print the results
print(f"\nBusiness Name: {business_name}")
print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {compound_interest}")