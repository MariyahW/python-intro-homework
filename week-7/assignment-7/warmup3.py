import os

print(f"\n{os.getcwd()} \n")

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
path = os.path.join("..", "data", "expenses.csv")
print(path)
