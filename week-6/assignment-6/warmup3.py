def showScope():
    x = 10  # Local variable
    return x
# NameError: name 'x' is not defined
# ans=x+5
print(f"answer is {showScope()+5}")  # Output: answer is 15