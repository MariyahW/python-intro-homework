import os

try:
    newPath= os.path.join("..","data","missing.txt")
    with open(newPath,'r') as file:
        print(file) 
    
except FileNotFoundError as err:
    print(f"{err}")