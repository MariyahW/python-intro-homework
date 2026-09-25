numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
# input_choice = 0
# max=-1
# min=100
# inList=False

def find_max(numbers):
    max=-1
    for n in numbers:
            if n>max:
                max=n
    print(f"The maximum number in the list is: {max}")
def find_min(numbers):
    min=100
    for n in numbers:
            if n<min:
                 min=n
    print(f"The minimum number in the list is: {min}")

def search_number(numbers, search):
    inList=False
    for n in numbers:
        if n==int(search) and inList==False:
            print(f"{search} is in the list at index {numbers.index(n)}.")
            inList=True
            break
    if inList==False:
        print(f"{search} is not in the list.")  
    
def sort_list(numbers):
    lengthy=len(numbers)
    for i in range(lengthy-1):
        for j in range(lengthy-i-1):
                if numbers[j]>numbers[j+1]:
                    numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers

def show_menu():
    
    print(f"++++++++ Number Cruncher ++++++++\n")
    print(f"1. Find Max")
    print(f"2. Find Minimum")
    print(f"3. Search for a number")
    print(f"4. Sort the list")
    print(f"5. Quit")
    return input("Enter your choice (1-5): ")
    
def main():
    input_choice=""
    while input_choice != "5":
        
        input_choice = show_menu()

        match input_choice:
            case "1":
                find_max(numbers)
            case "2":
                find_min(numbers)
            case "3":
                search=input("Enter a number to search for: ")
                search_number(numbers, search)
                # inList=False

            case "4":
                sorted_list = sort_list(numbers)
                print(f"The sorted list is: {sorted_list}")
                    
            case "5":
                print("Thank you for using the Number Cruncher!")
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    print(numbers) # remains unsorted