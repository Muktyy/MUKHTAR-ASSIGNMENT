business_name = """                                                           
 __ __             ___              _    _____             
|  |  |_ _ ___ _ _|  _|   ___ ___ _| |  |   __|___ ___ ___ 
|_   _| | |_ -| | |  _|  | .'|   | . |  |__   | . |   |_ -|
  |_| |___|___|___|_|    |__,|_|_|___|  |_____|___|_|_|___|
                                                           """

print(business_name)
principal = float(input("Enter the initial principal amount: "))
rate = float(input("Enter the interest rate (as a decimal): "))
time = int(input("Enter the number of time periods elapsed: "))
compound_periods = int(input("Enter the number of times interest is compounded per time period: "))

# Calculate simple interest
simple_interest = principal * (1 + rate * time)

# Calculate compound interest
compound_interest = principal * (1 + rate/compound_periods)**(compound_periods*time)

# Print the results
print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {compound_interest}")
