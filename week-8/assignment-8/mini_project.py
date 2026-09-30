import os
import csv
attempted=0
parsed=0
skipped=0
reasons=[]
try:
    tryPath=os.path.join("..","data","messy_data.csv")
    with open(tryPath,'r') as file:
        reader=csv.DictReader(file)
        try:
            for line in reader:
                print(line)
        except ValueError as val:
            skipped+=1
            reasons.append(line.ind)
            print(val)
except FileNotFoundError as err:
    print(err)
