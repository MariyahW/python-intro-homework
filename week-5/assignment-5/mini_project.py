numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
input_choice = 0
max=-1
min=100
while input_choice != "5":
    print(f"++++++++ Number Cruncher ++++++++\n")
    print(f"1. Find Max")
    print(f"2. Find Minimum")
    print(f"3. Search for a number")
    print(f"4. Sort the list")
    print(f"5. Quit")
    input_choice = input("Enter your choice (1-5): ")

    match input_choice:
        case "1":
            for n in numbers:
                if n>max:
                    max=n
            print(f"The maximum number in the list is: {max}")
        case "2":
            for n in numbers:
                if n<min:
                    min=n
            print(f"The minimum number in the list is: {min}")
        case "3":
            search=input("Enter a number to search for: ")
            for n in numbers:
                if n==int(search):
                    print(f"{search} is in the list at index {numbers.index(n)}.")
                    break
                else:
                    print(f"{search} is not in the list.")
                    break

        case "4":
            lengthy=len(numbers)
            for i in range(lengthy-1):
                for j in range(lengthy-i-1):
                    if numbers[j]>numbers[j+1]:
                        numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            print(f"The sorted list is: {numbers}")
                
        case "5":
            print("Thank you for using the Number Cruncher!")
        case _:
            print("Invalid choice. Please enter a number between 1 and 5.")