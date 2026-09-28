
    
while True:
    ans=input("Please enter a number: ")
    try:
        print(f"{float(ans)}")
        break
    except Exception as err:
        print(f"{err}: That's not a number. Try again")
