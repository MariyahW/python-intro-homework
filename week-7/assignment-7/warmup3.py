import os

print(f"\n{os.getcwd()} \n")

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found \n")
else:
    print("expenses.csv not found \n")
path = os.path.join("..", "data", "expenses.csv")
print(path)
