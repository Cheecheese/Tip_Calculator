print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 0%, 10%, 12%, or 15%? ")
people = input("How many people to split the bill? ")
each = round(float(bill) * (int(percent)/100+1) / int(people), 2)
print(f"Each person should pay: ${each}")