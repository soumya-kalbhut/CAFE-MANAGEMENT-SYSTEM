menu = {
    1: ("Coffee", 50),
    2: ("Tea", 30),
    3: ("Sandwich", 80),
    4: ("Pastry", 60),
    5: ("Burger", 120),
    6: ("Cold Drink", 40),
    7: ("Fries", 70),
}

print("===== WELCOME TO OUR CAFE =====")
print(f"{'No.':<5}{'Item':<15}{'Price (Rs)':<10}")
for key, (item, price) in menu.items():
    print(f"{key:<5}{item:<15}{price:<10}")

order = {}

while True:
    choice = int(input("\nEnter item number to order (0 to checkout): "))

    if choice == 0:
        break

    if choice not in menu:
        print("Invalid item number. Try again.")
        continue

    qty = int(input(f"Enter quantity for {menu[choice][0]}: "))
    order[choice] = order.get(choice, 0) + qty
    print(f"Added: {qty} x {menu[choice][0]}")

print("\n===== CAFE BILL =====")
print(f"{'Item':<15}{'Qty':<5}{'Rate':<7}{'Amount':<8}")

subtotal = 0
for item_no, qty in order.items():
    name, price = menu[item_no]
    amount = price * qty
    subtotal += amount
    print(f"{name:<15}{qty:<5}{price:<7}{amount:<8}")

tax = subtotal * 0.05
total = subtotal + tax

print("----------------------")
print(f"Subtotal: Rs {subtotal:.2f}")
print(f"Tax (5%): Rs {tax:.2f}")
print(f"Total:    Rs {total:.2f}")
print("Thank you for visiting!")



print("\n===== PAYMENT =====")
tip_choice = input("Would you like to add a 10% tip? (yes/no): ").lower()

if tip_choice == "yes" or tip_choice == "y":
    tip_amount = total * 0.10
    final_total = total + tip_amount
    print(f"Tip amount: Rs {tip_amount:.2f}")
    print(f"NEW TOTAL : Rs {final_total:.2f}")
else:
    final_total = total
    print(f"No tip added. Total remains: Rs {final_total:.2f}")

print("\nOrder complete! Have a great day!")



print("\n===== CUSTOMER FEEDBACK =====")
print("We value your feedback! Please rate us out of 5.")

ratings_array = []


categories = ["food", "service", "speed of service"]


for category in categories:
    while True:
       
        rating = int(input(f"Rate the {category} (1-5): "))
        
       
        if 1 <= rating <= 5:
            ratings_array.append(rating)
            break 
        else:
            print("Invalid rating! Please enter a number between 1 and 5.")

print("\n--- Feedback Summary ---")
print(f"Your ratings array: {ratings_array}")

average_rating = sum(ratings_array) / len(ratings_array)
print(f"Your Average Rating: {average_rating:.1f} out of 5.0")
print("Thank you! We hope to see you again.")