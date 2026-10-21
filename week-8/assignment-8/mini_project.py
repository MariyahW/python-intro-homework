import os
import csv

parsed = 0
skipped = 0
reasons = []
worked = []

try:
    tryPath = os.path.join("..", "data", "messy_data.csv")
    with open(tryPath, "r") as file:
        reader = csv.DictReader(file, restkey="extra")

        for row_num, line in enumerate(reader, start=1):
            try:
                if line.get("extra"):
                    raise ValueError("extra column detected — skipped")

                worked.append(
                    {
                        "name": line["name"],
                        "category": line["category"],
                        "amount": float(line["amount"]),
                    }
                )
                parsed += 1

            except ValueError as val:
                skipped += 1
                # FIX 2: Better exception formatting
                reasons.append(f"Row {row_num}: ValueError — {val}")
            except KeyError as k:
                skipped += 1
                reasons.append(f"Row {row_num}: KeyError — missing key {k}")

except FileNotFoundError as err:
    print(err)


attempted = parsed + skipped

# FIX 3: Structured report format
print("=== CSV Report ===")
print(f"Rows attempted: {attempted}")
print(f"Rows parsed: {parsed}")
print(f"Rows skipped: {skipped}")

print("\nSkipped rows:")
for reason in reasons:
    print(f"- {reason}")


print("\nClean data:")
for work in worked:

    print(f"- {work['name']} | {work['category']} | ${work['amount']:.2f}")
