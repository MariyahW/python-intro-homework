import os
import csv
from datetime import datetime
foodItems=[]
total=0
# cat=input("Which category are you searching for?")
try:
    path=os.path.join("..","data","expenses.csv")
    if os.path.exists(path):
        with open(path,'r') as file:
            reader =csv.DictReader(file)
            for row in reader:
                row["amount"]=float(row["amount"])
                if row["category"].lower()=='food':
                    foodItems.append(row)
                # print(row)
                # print(foodItems)
    for item in foodItems:
        total+=item["amount"]
    # print(total)
    curDate=datetime.now().strftime("%B %d, %Y")
    with open("../data/food_report.txt","w") as file:
        file.write(f"Food expense Report generated - {curDate}\n")
        for item in foodItems:
            file.write(f"{item["date"]}: {item["amount"]}\n")
        file.write(f"Total: ${total:.2f}")
except Exception as error:
    print(error)

