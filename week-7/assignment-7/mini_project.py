import os
import csv
from datetime import datetime

cat = input("Which category are you searching for? ")
path = os.path.join("..", "data", "expenses.csv")

try:
    if not os.path.exists(path):
        print("file does not exist")
        exit()

    items = []
    total = 0

    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            if row["category"].lower() == cat.lower():
                items.append(row)

    for item in items:
        total += item["amount"]

    curDate = datetime.now().strftime("%B %d, %Y")
    report_path = os.path.join("..", "data", f"{cat}_report.txt")

    with open(report_path, "w") as file:
        file.write(f"{cat} expense Report generated - {curDate}\n")
        for item in items:
            file.write(f"{item['date']}: ${item['amount']:.2f}\n")
        file.write(f"Total: ${total:.2f}")

except Exception as error:
    print(error)
