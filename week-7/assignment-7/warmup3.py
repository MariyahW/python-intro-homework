import os
print(f"\n{os.getcwd()} \n")

if os.path.exists("../data/expenses.csv"):
    print("found it \n")
else:
    print("nope \n")
path=os.path.join("..","data","expenses.csv")
print(path)