num=input("Enter the numerator: ")
denom=input("Thanks, now enter the denominator: ")
try:
    ans=float(num)/float(denom)
    print(f"{num}/{denom}={ans}")
except ZeroDivisionError:
    print("Sorry you cannot divide by 0.")
except Exception as e:
    print(f"{e}")