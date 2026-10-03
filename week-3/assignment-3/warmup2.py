age = int(input("Please enter your age: "))
if age >= 65:
    print("You are a senior.")
elif age >= 18 and int(age) < 65:
    print("You are an adult.")
elif age < 18 and int(age) >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
