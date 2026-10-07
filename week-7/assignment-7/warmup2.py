import csv

with open("python-intro-homework/week-7/data/students.csv",'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(f"{row["name"]}: {row["score"]}")