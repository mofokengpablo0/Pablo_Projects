
from pathlib import Path

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """Initialize a Shoe with country, code, product, cost, and quantity."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of this shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of this shoe."""
        return self.quantity

    def __str__(self):
        """Return a formatted string representation of this shoe."""
        return (
            f"{self.country:20} | {self.code:10} | {self.product:20} | "
            f"R{self.cost:8.2f} | {self.quantity:5}"
        )


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
INVENTORY_FILE = Path(__file__).parent / "inventory.txt"


#==========Functions outside the class==============
def read_shoes_data():
    """Load shoe data from inventory.txt into shoe_list."""
    try:
        with INVENTORY_FILE.open("r", encoding="utf-8") as file:
            next(file)  # Skip the header line
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
                    shoe_list.append(shoe)
        print("✓ Shoe data loaded successfully!")
    except FileNotFoundError:
        print("Error: inventory.txt file not found!")
    except Exception as e:
        print(f"Error reading file: {e}")

def capture_shoes():
    """Capture new shoe details from the user and add them to shoe_list."""
    try:
        country = input("Enter the country of manufacture: ")
        code = input("Enter the product code: ")
        product = input("Enter the product/brand name: ")
        cost = input("Enter the cost: ")
        quantity = input("Enter the quantity: ")
        
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("✓ Shoe added successfully!\n")
    except ValueError:
        print("Error: Invalid input. Please check your entries.\n")
    except Exception as e:
        print(f"Error: {e}\n")

def view_all():
    """Print all shoes currently stored in shoe_list."""
    if not shoe_list:
        print("No shoes in inventory!\n")
        return
    
    print("\n" + "="*85)
    print(
        f"{'Country':20} | {'Code':10} | {'Product':20} | "
        f"{'Cost':8} | {'Qty':5}"
    )
    print("="*85)
    for shoe in shoe_list:
        print(shoe)
    print("="*85 + "\n")


def re_stock():
    """Find the lowest-quantity shoe, update its quantity, and save the file."""
    if not shoe_list:
        print("No shoes in inventory!\n")
        return
    
    # Find shoe with lowest quantity
    lowest_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    
    print(
        f"\n⚠ Shoe with lowest quantity: {lowest_shoe.product} "
        f"(Code: {lowest_shoe.code})"
    )
    print(f"Current quantity: {lowest_shoe.quantity}")
    
    try:
        add_quantity = int(input("How many units would you like to add? "))
        lowest_shoe.quantity += add_quantity
        print(f"✓ Quantity updated! New quantity: {lowest_shoe.quantity}\n")
        
        # Update the file
        update_inventory_file()
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def search_shoe():
    """Search shoe_list by code and display the matching shoe."""
    if not shoe_list:
        print("No shoes in inventory!\n")
        return
    
    code = input("Enter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            print(f"\n✓ Shoe found:")
            print("="*85)
            print(
                f"{'Country':20} | {'Code':10} | {'Product':20} | "
                f"{'Cost':8} | {'Qty':5}"
            )
            print("="*85)
            print(shoe)
            print("="*85 + "\n")
            return shoe
    
    print(f"✗ No shoe found with code: {code}\n")
    return None

def value_per_item():
    """Calculate and print the total value for each shoe item."""
    if not shoe_list:
        print("No shoes in inventory!\n")
        return
    
    print("\n" + "="*90)
    print(
        f"{'Product':20} | {'Code':10} | {'Cost':10} | "
        f"{'Quantity':10} | {'Total Value':15}"
    )
    print("="*90)
    
    total_inventory_value = 0
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        total_inventory_value += value
        print(
            f"{shoe.product:20} | {shoe.code:10} | R{shoe.cost:9.2f} | "
            f"{shoe.quantity:10} | R{value:14.2f}"
        )
    
    print("="*90)
    print(f"{'TOTAL INVENTORY VALUE:':52} R{total_inventory_value:14.2f}")
    print("="*90 + "\n")

def highest_qty():
    """Print the shoe with the highest quantity as the sale item."""
    if not shoe_list:
        print("No shoes in inventory!\n")
        return
    
    highest_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    
    print("\n" + "="*85)
    print("🔥 ON SALE - HIGHEST QUANTITY ITEM 🔥")
    print("="*85)
    print(f"Product: {highest_shoe.product}")
    print(f"Code: {highest_shoe.code}")
    print(f"Country: {highest_shoe.country}")
    print(f"Cost: R{highest_shoe.get_cost():.2f}")
    print(f"Available Quantity: {highest_shoe.get_quantity()}")
    print("="*85 + "\n")


def update_inventory_file():
    """Write the current inventory from shoe_list back to inventory.txt."""
    try:
        with INVENTORY_FILE.open("w", encoding="utf-8") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as e:
        print(f"Error updating file: {e}\n")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

def display_menu():
    print("\n" + "="*50)
    print("     🏀 SHOE INVENTORY MANAGEMENT SYSTEM 🏀     ")
    print("="*50)
    print("1. Read shoe data from file")
    print("2. Add new shoe")
    print("3. View all shoes")
    print("4. Restock lowest quantity item")
    print("5. Search for a shoe")
    print("6. View value per item")
    print("7. View highest quantity item for sale")
    print("8. Save and Exit")
    print("="*50)

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            print("\n✓ Saving data and exiting...")
            update_inventory_file()
            print("Thank you for using the Shoe Inventory System!")
            break
        else:
            print("❌ Invalid choice! Please select 1-8.\n")

# End of inventory.py
# fixed the path naming issue and with the aid of recommended extentions ,i managed to do some fixing regarding the PEP8 styling issue.            