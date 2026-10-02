num = input("Please enter a number: ")
if int(num) > 0:
    print("The number is positive.")
elif int(num) == 0:
    print("You entered 0, neither negative or positive")
else:
    print("The number is negative.")
if int(num) % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
