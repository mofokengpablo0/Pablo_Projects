"""
╔════════════════════════════════════════════════════════════════════════════╗
║                   SHOE INVENTORY SYSTEM - IMPLEMENTATION GUIDE             ║
║                                                                            ║
║ This file explains how the inventory.py solution was built step-by-step   ║
╚════════════════════════════════════════════════════════════════════════════╝

## PART 1: THE SHOE CLASS
═════════════════════════════════════════════════════════════════════════════

The Shoe class is the foundation of our system. Here's how it was designed:

1. ATTRIBUTES (Instance Variables)
   ─────────────────────────────────
   - country:  Where the shoe is manufactured (string)
   - code:     Product SKU/code for identification (string)
   - product:  Brand or model name (string)
   - cost:     Price per unit (converted to float for calculations)
   - quantity: Number of units in stock (converted to int for counting)

   Example: Shoe("South Africa", "SKU44386", "Air Max 90", 2300, 20)

2. __init__ METHOD
   ────────────────
   - Initializes all attributes when a Shoe object is created
   - IMPORTANT FIX: The original code had "pass" statements that did nothing
   - SOLUTION: Removed "pass" and added proper initialization logic
   - Type conversion: Convert cost to float and quantity to int for proper
     arithmetic operations (multiplying numbers, finding min/max)

3. get_cost() METHOD
   ──────────────────
   - ORIGINAL BUG: Used "self.get_cost = self.cost" (assignment instead of return)
   - FIX: Changed to "return self.cost"
   - WHY: This method needs to RETURN a value, not assign to itself
   - USAGE: Used in value_per_item() to calculate total inventory value

4. get_quantity() METHOD
   ──────────────────────
   - ORIGINAL BUG: Used "self.get_quantity = self.quantity" (assignment)
   - FIX: Changed to "return self.quantity"
   - USAGE: Used in re_stock() to find lowest quantity & value_per_item()

5. __str__() METHOD
   ─────────────────
   - ORIGINAL: Returned tuple notation: (country, code, product, cost, quantity)
   - IMPROVEMENT: Formatted as a table row with aligned columns
   - FORMAT: Fixed-width columns for better presentation
   - BENEFITS: 
     * Looks professional when printed in view_all()
     * Easy to read in tabular format
     * All attributes visible at once


## PART 2: DATA STRUCTURES
═════════════════════════════════════════════════════════════════════════════

1. shoe_list = []
   ────────────────
   - Global list that stores all Shoe objects
   - Starts empty and gets populated by read_shoes_data()
   - Every Shoe created with capture_shoes() is appended here
   - All functions operate on this list


## PART 3: CORE FUNCTIONS
═════════════════════════════════════════════════════════════════════════════

1. read_shoes_data()
   ──────────────────
   PROBLEM: Need to read CSV data from inventory.txt file
   
   SOLUTION STEPS:
   a) Try-Except Block: Handles FileNotFoundError if file doesn't exist
   
   b) File Reading:
      with open(...) as file:
          - Opens inventory.txt in read mode ("r")
          - Uses context manager (with statement) for automatic file closing
   
   c) Skip Header:
      next(file)
      - Reads and discards first line (Country,Code,Product,Cost,Quantity)
      - Why: The header is not data, we don't want to create a Shoe from it
   
   d) Parse CSV Data:
      for line in file:
          data = line.strip().split(',')
          - strip() removes newline characters at end of line
          - split(',') splits by comma into 5 elements: [0]=country, [1]=code,
            [2]=product, [3]=cost, [4]=quantity
   
   e) Create Shoe Objects:
      shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
      - Instantiates new Shoe with parsed data
      - The Shoe.__init__() handles type conversion (cost→float, qty→int)
   
   f) Store in List:
      shoe_list.append(shoe)
      - Adds each Shoe object to the global shoe_list
   
   RESULT: After function runs, shoe_list contains 24 Shoe objects (from file)


2. capture_shoes()
   ────────────────
   PROBLEM: Allow user to manually enter shoe data
   
   SOLUTION STEPS:
   a) Input Collection:
      - Ask user for country, code, product, cost, quantity
      - Use input() for each field
      - All inputs are strings initially
   
   b) Shoe Object Creation:
      shoe = Shoe(country, code, product, cost, quantity)
      - Pass all inputs to Shoe.__init__()
      - Type conversion happens in Shoe class
   
   c) Append to List:
      shoe_list.append(shoe)
      - New shoe is added to inventory
   
   d) Error Handling:
      - ValueError: Catches if user enters non-numeric values for cost/quantity
      - General Exception: Catches any other unexpected errors
      - User receives helpful error message
   
   WHY NO FILE UPDATE? The file is updated only when user exits (choice 8)


3. view_all()
   ──────────
   PROBLEM: Display all shoes in a readable format
   
   SOLUTION STEPS:
   a) Check if shoe_list is empty:
      if not shoe_list:
      - Prevents error and informs user
   
   b) Print Table Header:
      - Print "=" borders for visual separation
      - Print column headers (Country, Code, Product, Cost, Qty)
      - Print "=" borders
   
   c) Iterate and Print:
      for shoe in shoe_list:
          print(shoe)
      - Calls __str__() method on each Shoe object
      - Our __str__() format ensures clean table rows
   
   d) Close Table:
      - Print final "=" border
   
   RESULT: All shoes displayed as a formatted table


4. re_stock()
   ──────────
   PROBLEM: Find the shoe with lowest quantity and allow restocking
   
   SOLUTION STEPS:
   a) Find Minimum:
      lowest_shoe = min(shoe_list, key=lambda x: x.get_quantity())
      - Iterates through all shoes
      - key=lambda x: x.get_quantity() tells min() to compare by quantity
      - Returns the Shoe object with smallest quantity value
   
   b) Display Information:
      - Show which shoe has lowest quantity
      - Show current quantity
   
   c) Get User Input:
      add_quantity = int(input(...))
      - Ask how many units to add
      - int() converts string input to integer
   
   d) Update Quantity:
      lowest_shoe.quantity += add_quantity
      - Adds the new quantity to existing quantity
      - Example: if quantity was 4 and user adds 96, new quantity = 100
   
   e) Save to File:
      update_inventory_file()
      - Writes updated data back to inventory.txt
   
   WHY: This is the only function that modifies file immediately because
        it's a critical restock operation


5. search_shoe()
   ──────────────
   PROBLEM: Find a specific shoe by its code
   
   SOLUTION STEPS:
   a) Get Search Code:
      code = input("Enter the shoe code to search: ")
   
   b) Iterate Through List:
      for shoe in shoe_list:
          if shoe.code.lower() == code.lower():
      - Compares shoe codes
      - .lower() makes comparison case-insensitive (SKU44386 = sku44386)
   
   c) Found Match:
      - Display the shoe in formatted table row
      - Return the Shoe object (for possible future use)
   
   d) No Match:
      print(f"✗ No shoe found with code: {code}\n")
      - Inform user and return None
   
   BENEFIT: Case-insensitive search is user-friendly


6. value_per_item()
   ─────────────────
   PROBLEM: Calculate and display inventory value for each shoe
   
   KEY FORMULA: value = cost × quantity
   
   SOLUTION STEPS:
   a) Create Table Header:
      - Print column headers (Product, Code, Cost, Quantity, Total Value)
   
   b) Iterate Through Shoes:
      for shoe in shoe_list:
          value = shoe.get_cost() * shoe.get_quantity()
          - Multiply unit cost by quantity to get total value for that item
          - Uses get_cost() and get_quantity() methods for data access
   
   c) Accumulate Total:
      total_inventory_value += value
      - Keeps running sum of all item values
   
   d) Print Each Row:
      print(f"{shoe.product:20} | {shoe.cost:9.2f} | ...")
      - Formats numbers with specific decimal places (2 decimals)
      - Aligns columns for readability
   
   e) Print Grand Total:
      - Shows sum of all inventory values
   
   BUSINESS VALUE: Managers see exactly how much money is tied up in inventory


7. highest_qty()
   ──────────────
   PROBLEM: Find the shoe with most units available
   
   SOLUTION STEPS:
   a) Find Maximum:
      highest_shoe = max(shoe_list, key=lambda x: x.get_quantity())
      - Similar to min() but finds maximum quantity
   
   b) Display Prominently:
      - Print special formatting ("🔥 ON SALE 🔥")
      - Show all details: Product, Code, Country, Cost, Quantity
      - Highlight this is the item available in highest quantities
   
   BUSINESS APPLICATION: Marketing can use this to promote overstocked items


## PART 4: HELPER FUNCTION
═════════════════════════════════════════════════════════════════════════════

update_inventory_file()
───────────────────────
PROBLEM: When data changes, we need to persist it back to file

SOLUTION STEPS:
a) Open File for Writing:
   open(..., "w")
   - "w" mode truncates (clears) the file before writing

b) Write Header:
   file.write("Country,Code,Product,Cost,Quantity\n")
   - Reconstructs the CSV header line

c) Write All Shoes:
   for shoe in shoe_list:
       file.write(f"{shoe.country},{shoe.code},{shoe.product},...\n")
   - Loops through shoe_list
   - Uses f-string to format each shoe data as CSV row
   - Each line becomes one shoe record

d) Error Handling:
   try-except catches file write errors

TIMING: Called when:
- User restock shoes (re_stock function)
- User exits program (menu choice 8)


## PART 5: MAIN MENU SYSTEM
═════════════════════════════════════════════════════════════════════════════

1. display_menu()
   ───────────────
   - Prints a formatted menu with 8 options
   - Uses visual separators for clarity
   - Shows emoji for branding

2. Main Loop (if __name__ == "__main__":)
   ──────────────────────────────────────
   WHY "if __name__ == '__main__':"?
   - This line checks if the script is run directly (not imported)
   - Allows clean module reuse in other projects
   - Good professional practice

3. Infinite While Loop (while True:)
   ─────────────────────────────────
   - Keeps program running until user chooses exit
   - Shows menu before each choice
   - Processes user input

4. Menu Choices (if-elif-elif...):
   ────────────────────────────────
   Choice 1: read_shoes_data()     → Load file data
   Choice 2: capture_shoes()       → Manual entry
   Choice 3: view_all()            → Display inventory
   Choice 4: re_stock()            → Find & restock
   Choice 5: search_shoe()         → Find by code
   Choice 6: value_per_item()      → Calculate values
   Choice 7: highest_qty()         → Show bestseller
   Choice 8: Save & Exit           → Update file & quit
   Default: Show error message

5. Input Validation:
   strip() removes whitespace
   Only processes valid choices 1-8


## PART 6: KEY PROGRAMMING CONCEPTS USED
═════════════════════════════════════════════════════════════════════════════

1. Object-Oriented Programming (OOP)
   - Shoe class encapsulates shoe data and behavior
   - __init__(), get_cost(), get_quantity(), __str__() are methods
   - Objects created from class blueprint

2. File I/O (Input/Output)
   - Reading: open() in "r" mode
   - Writing: open() in "w" mode
   - Context manager: with statement for auto-closing

3. Error Handling
   - try-except blocks catch exceptions
   - Graceful failure instead of program crash
   - User-friendly error messages

4. Data Structures
   - Lists store multiple Shoe objects
   - Combined with loops for batch operations

5. String Formatting
   - f-strings for readable output: f"{variable:width.decimals}"
   - split() and join() for CSV parsing

6. Built-in Functions
   - min(): finds Shoe with lowest quantity
   - max(): finds Shoe with highest quantity
   - Both use lambda functions for custom comparison

7. Lambda Functions
   - Anonymous functions used as keys: lambda x: x.get_quantity()
   - Enables sorting/finding by specific attribute


## PART 7: FLOW EXAMPLE
═════════════════════════════════════════════════════════════════════════════

Typical user session:

   1. Program starts → Main menu displayed
   2. User enters "1" → read_shoes_data() loads 24 shoes from inventory.txt
   3. User enters "3" → view_all() displays all shoes in table format  
   4. User enters "6" → value_per_item() shows total inventory value
   5. User enters "4" → re_stock() finds lowest qty (AIR YEEZY 2 SKU77999 with 67)
                       User adds 33 units → quantity becomes 100
                       update_inventory_file() saves to file
   6. User enters "8" → Program saves and exits
   7. File inventory.txt now has updated quantity for Air Yeezy 2


## PART 8: IMPROVEMENTS MADE TO ORIGINAL CODE
═════════════════════════════════════════════════════════════════════════════

BUGS FIXED:
1. ✓ Removed "pass" statements that prevented code execution
2. ✓ Fixed get_cost() to return instead of assign
3. ✓ Fixed get_quantity() to return instead of assign  
4. ✓ Fixed read_shoes_data() to READ not WRITE file
5. ✓ Fixed view_all() file reading logic
6. ✓ Added proper type conversions (cost→float, qty→int)

FEATURES ADDED:
1. ✓ Proper CSV parsing with header skip
2. ✓ Exception handling in critical functions
3. ✓ File updating capability
4. ✓ Formatted table output for professional presentation
5. ✓ Complete menu system with error validation
6. ✓ Search functionality with case-insensitive matching
7. ✓ Inventory value calculations
8. ✓ Highlighted "for sale" item display
9. ✓ Helper function for file persistence
10. ✓ User-friendly prompts and confirmations


## PART 9: HOW TO USE THE SYSTEM
═════════════════════════════════════════════════════════════════════════════

Step 1: Run the program
   python inventory.py

Step 2: Read shoe data
   Enter choice: 1
   → Loads all 24 shoes from inventory.txt

Step 3: View inventory
   Enter choice: 3
   → See all shoes in table format

Step 4: Check inventory value
   Enter choice: 6
   → See cost × quantity for each item
   → See total inventory value

Step 5: Restock
   Enter choice: 4
   → Find and restock the lowest quantity item
   → Updates happen in memory AND file

Step 6: Search for specific shoe
   Enter choice: 5
   → Find shoe by code (case-insensitive)

Step 7: View bestseller
   Enter choice: 7
   → See shoe with highest quantity available

Step 8: Exit
   Enter choice: 8
   → Saves all data to inventory.txt
   → Program ends


═════════════════════════════════════════════════════════════════════════════
End of Implementation Guide - Questions? Check the comments in inventory.py!
═════════════════════════════════════════════════════════════════════════════
"""

# Code examples of key concepts:

def example_lambda_functions():
    """
    Lambda functions are small anonymous functions used in min/max operations.
    
    Syntax: lambda arguments: expression
    
    Examples:
    """
    shoes = []  # Imagine this has Shoe objects
    
    # Finding minimum quantity
    # Instead of: for shoe in shoes: if shoe.quantity is lowest...
    # We use: min(shoes, key=lambda x: x.get_quantity())
    
    # Finding maximum value
    # Instead of: for shoe in shoes: if shoe value is highest...
    # We use: max(shoes, key=lambda x: x.cost * x.quantity)
    
    print("Lambda functions make finding min/max elegant and efficient!")


def example_csv_parsing():
    """
    CSV (Comma-Separated Values) files look like:
    
    Country,Code,Product,Cost,Quantity
    South Africa,SKU44386,Air Max 90,2300,20
    China,SKU90000,Jordan 1,3200,50
    
    To parse one line:
    """
    line = "South Africa,SKU44386,Air Max 90,2300,20"
    
    data = line.strip().split(',')
    
    # Result: ['South Africa', 'SKU44386', 'Air Max 90', '2300', '20']
    # data[0] = 'South Africa'
    # data[1] = 'SKU44386'
    # data[2] = 'Air Max 90'
    # data[3] = '2300'
    # data[4] = '20'
    
    print("CSV parsing separates data with split(',') after removing whitespace!")


def example_f_string_formatting():
    """
    F-strings format numbers with specific widths and decimal places.
    
    Syntax: f"{variable:width.decimals}"
    """
    product = "Air Max 90"
    price = 2300.00
    quantity = 20
    
    # Print in table format:
    # f"{product:20}" → "Air Max 90        " (20-char wide, left-aligned)
    # f"{price:9.2f}" → "  2300.00" (9-char wide, 2 decimals, right-aligned)
    # f"{quantity:10}" → "        20" (10-char wide, right-aligned)
    
    print(f"{product:20} | {price:9.2f} | {quantity:10}")
    # Output: "Air Max 90           |   2300.00 |         20"
    
    print("F-string formatting creates professional-looking tables!")


if __name__ == "__main__":
    print(__doc__)
    print("\n" + "="*80)
    print("Additional code examples:")
    print("="*80 + "\n")
    
    example_lambda_functions()
    print()
    example_csv_parsing()
    print()
    example_f_string_formatting()
