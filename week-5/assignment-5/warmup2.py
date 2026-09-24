num=-1
try:
    while num<0:
        num=int(input("Enter a positive number: "))
        if num<0:
            print("That is not a positive number. Lets do that again.")
    print(f"Awesome! You entered {num}.")
except:
    print("Invalid input. Please enter a valid integer.")