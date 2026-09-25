# A function to show the scope of a variable
def showScope():
    x = 10  # Local variable
    return x
# NameError: name 'x' is not defined
# ans=x+5

ans=showScope()
print(f"answer is {ans+5}")  # Output: answer is 15

