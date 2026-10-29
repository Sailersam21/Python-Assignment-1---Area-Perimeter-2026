# Fence Cost Calculator​
# Sam Francis-Stead 
# Oct 28 2026


def calculate_fencing_cost():
    while True:
        print()
        print("---welcome to the fencing Cost Calculator---\n")
        try:
# Ask for the length width and cost
            length = float(input("Enter the length of the fence (in meters): "))
            width = float(input("Enter the width of the fence (in meters): "))
            cost_per_meter = float(input("Enter the cost of the fence per meter : $"))
            
# Perimeter of a rectangle = 2 * (length + width)
            
            perimeter = 2 * (length + width)
            total_cost = perimeter * cost_per_meter
            
            print(f" Perimeter: {perimeter} meters \n")
            print(f"Total Cost of Fencing: ${total_cost}")
            break
            
        except ValueError:
            print("Please enter valid numeric values.")

# Asking if the persons wants to perform another calculation
       
        
            
 
# Main routine. 
calculate_fencing_cost()
while True:
    choice = input("Do you want to perform another calculation? (y/n): ").lower()
    if choice == "y" :
        calculate_fencing_cost()
    elif choice == "n":
        break
    
    else:
        print ("Please enter either y or n.")


print("Exiting the program. Goodbye!\n")           








            
