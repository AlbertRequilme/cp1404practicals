"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
HIGH_BONUS_RATE = 0.15
LOW_BONUS_RATE = 0.10
print("Please input your sales. Type a negative number to end the program.")
sales_in_dollars = float(input("Sales: "))
while sales_in_dollars >=0:
    high_bonus = sales_in_dollars * HIGH_BONUS_RATE
    low_bonus = sales_in_dollars * LOW_BONUS_RATE
    message = "The user gets:"
    if sales_in_dollars >= 1000:
        print(message,high_bonus)
        sales_in_dollars = float(input("Sales: "))
    elif sales_in_dollars < 1000:
        print(message,low_bonus)
        sales_in_dollars = float(input("Sales: "))
print("Thanks for using this program!")