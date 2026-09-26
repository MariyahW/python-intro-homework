import os
import csv
from datetime import datetime
items=[]
total=0
cat=input("Which category are you searching for?")
try:
    path=os.path.join("..","data","expenses.csv")
    if os.path.exists(path):
        with open(path,'r') as file:
            reader =csv.DictReader(file)
            for row in reader:
                row["amount"]=float(row["amount"])
                if row["category"].lower()==cat.lower():
                    items.append(row)
                # print(row)
                # print(items)
    for item in items:
        total+=item["amount"]
    # print(total)
    curDate=datetime.now().strftime("%B %d, %Y")
    with open(f"../data/{cat}_report.txt","w") as file:
        file.write(f"{cat} expense Report generated - {curDate}\n")
        for item in items:
            file.write(f"{item["date"]}: {item["amount"]}\n")
        file.write(f"Total: ${total:.2f}")
except Exception as error:
    print(error)

