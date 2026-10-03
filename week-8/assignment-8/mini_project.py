import os
import csv

attempted = 0
parsed = 0
skipped = 0
reasons = []
worked = []
try:
    tryPath = os.path.join("..", "data", "messy_data.csv")
    with open(tryPath, "r") as file:
        reader = csv.DictReader(file)

        temp = ""
        for line in reader:
            attempted += 1
            try:
                worked.append(
                    (f"{line["name"]} | {line["category"]} | {float(line["amount"])} ")
                )
                parsed += 1

            except ValueError as val:
                skipped += 1

                reasons.append(f"Row {attempted}: {val}")
                # print(val)
            except KeyError as k:
                skipped += 1

                reasons.append(f"Row {attempted}: {k}")
except FileNotFoundError as err:
    print(err)
print(f"Attempted: {attempted} Parsed: {parsed} Skipped: {skipped}")
for reason in reasons:
    print(reason)
for work in worked:
    print(work)
