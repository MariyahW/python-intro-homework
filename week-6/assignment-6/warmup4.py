def is_valid_score(score):
    if score >=0 and score <=100:
        return True
    else:
        return False

num=input("Enter a score between 0 and 100: ")
try:
    if is_valid_score(int(num)):
        print("Valid score")
    else:
        print("Invalid score")
except ValueError:
    print("Invalid input. Please enter a numeric value.")