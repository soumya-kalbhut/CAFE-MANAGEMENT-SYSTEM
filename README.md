# Cafe food ordering system

An interactive "command_line interfce application" nuilt in python that simulates a digital restro/cafe menu and billing system.
This system will allow the cuustomers to view a menu, and add the items in specified quantities , and generate a bill by itself.

## PROBLEM STATEMENT
    Traditional manual billing systems used by small food stalls or canteens are slow, inaccurate, inconvenient for rush hours,and has tax caculation errors.

# ***solution
this project will provide the user a dedicated system which will manage the menue(automated menu),dynamic customer shopping cart,which will help in the generation of an errorless bill.

# CORE CONCEPTS USED/DEMOSTRATED
# 1--->DATA STURCTURES:
Dictionaries:(dict)used for structured data storage

    menu:A dictionary mapping an integer ID  to a tuple containing the item name and price .

    order:A dictionary that tracks the user's selected items, mapping the item ID to the chosen quantity.

tupples: Used inside the menu dictionary (("Coffee", 50)) to store immutable pairs of fixed data (Item Name, Price).

# 2--->CONTROL FLOW AND LOOPS
Infinite loop : allows the user to keep the program running infinite number of times untill the user decides to stop.

Loop control statement:
    break:immediately exits from the program(from the while loop) after the use of a trigger
    continue:skips the rest of the loop iteration and jumps back in the original prompt.

Conditional statements(if/elif/else):Validates user inputs.

Definite Loop(for):here the definite for loop is used two times--->
first to display the menu and later to loop tjrough the user's order to calculate and print the bill.

# 3 USER INPUT AND TYPE CASTING
    Input :captures text from the console.
    Type casting: converts the default string into output of input() 

# 4 STRING FORMATTING AND ALIGNMENT
    F-string(f"...."):embedded expressions inside string liberals for clean text interpolation

# 5 DICIONARY METHODS AND ARITHMETIC OPERATIONS
    The .get() method: it looks up an existing item quantity in the order.If the item hasn't been ordered yet , it safely returns 0 instead of throwing an error.
    Compound assignment(+=):used to accumulate values 
    Floating-points formatting
    
