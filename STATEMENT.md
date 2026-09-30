# Project Cafe Billing and Feedback System

## Objective

To create a Python program that runs in the terminal. This program will act like a cafes ordering system. It will help calculate the bill, including taxes and tips if needed. It will also collect feedback from customers after they order.

## The Program Requirements

### 1. Menu and Orders

The program starts by showing a menu with least seven items. Each item has a code number and a price in Rupees (RS). The customer can choose items by entering the item code. How many they want. If the user types a code the program will show an error message and ask again. The customer can keep adding items until they type 0 to finish the order.

### 2. Bill

Once the customer finishes ordering the program shows a list of all the items they ordered. It includes the quantity, rate per item and total cost for each. Then it calculates the subtotal. The sum of all costs before tax. Next it adds a 5% tax to the subtotal. The new amount including tax is shown to the customer.

### 3. Tips

After showing the amount with tax the program asks the customer if they want to add a 10% tip. If the customer says yes the tip is added to the total. If no the amount stays as it is. Either way the final amount is displayed.

### 4. Feedback

Now the program asks the customer to rate their experience. They must give a rating from 1 to 5 for three things: food, service and speed. If the user enters anything than a whole number between 1 and 5 the program shows an error and asks again. All ratings are saved in a list. After collecting all three ratings the program displays the list. Calculates the average rating rounding it to one decimal place.

## Sample Usage

1. The program welcomes the customer. Shows the menu.

2. The customer enters item code 1 and quantity 2 for Coffee.

3. Then the customer enters item code 5 and quantity 1 for Burger.

4. The customer types 0 to end the order.

5. The program lists all the ordered items with quantities, prices and totals. It then shows the subtotal.

6. The program adds 5% tax. Shows the updated amount.

7. The program asks if the customer wants to add a 10% tip. The customer says yes.

8. The tip is. The new final amount is shown.

9. The program asks for ratings, on food, service and speed.

10. The program prints the list of ratings and the average rating rounded to one place.