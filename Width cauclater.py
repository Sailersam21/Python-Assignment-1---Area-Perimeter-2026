# Width cauclater
# Sam Francis-Stead
# 21 Oct 2026

# Ask user for width and loop until they
# enter a number that is more than zero

print("Welcome to the width cauclater")
print()
print("Please enter your width")

error = "Please enter a number that is greater then zero\n"
while True:
    
    try:
        width = float(input("Width: "))

        if width > 0:
            break
        else:
            print(f"{error}")

    except ValueError:
        print(f"{error}")
