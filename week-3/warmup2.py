age=input("Please enter your age: ")
if int(age)>=65:
    print("You are a senior.")
elif int(age)>=18 and int(age)<65:
    print("You are an adult.")
elif int(age)<18 and int(age)>=13:
    print("You are a teenager.")
else:
    print("You are a child.")