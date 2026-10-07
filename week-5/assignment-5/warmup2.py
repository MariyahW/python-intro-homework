num = -1

while num < 1:
    try:
        num = int(input("Enter a positive number: "))
        if num < 1:
            print("That is not a positive number. Lets do that again.")
    except:
        print("Invalid input. Please enter a valid integer.")
print(f"Awesome! You entered {num}.")
