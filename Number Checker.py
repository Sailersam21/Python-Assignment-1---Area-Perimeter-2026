# Width cauclater
# Sam Francis-Stead
# 21 Oct 2026

# Ask user for width and loop until they
# enter a number that is more than zero

print("Welcome to the width cauclater")
print()
print("Please enter your width")

def num_check (question):
    error = "Please enter a number that is greater then zero\n"
    while True:
    
        try:
            response = float(input(question ))

            if response > 0:
                return response
            else:
        
                 print(f"{error}")

        except ValueError:
            print(f"{error}")

# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()


for item in range(0, 2):
    height = num_check("Height: ")
    print(height)
