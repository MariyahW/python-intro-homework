names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy",
]
counter = 0
check_name = input("Enter a name to check if it is in the list: ")
check_name_lower = check_name.lower()
in_list = False
for name in names:
    if name.lower() == check_name_lower:

        print(f"{check_name} is in the list at index {counter}.")
        in_list = True
        break
    counter += 1
if not in_list:
    print(f"{check_name} is not in the list.")
