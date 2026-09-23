# Commands python-intro-homework/week-2/assignment-2/
#  touch warmup2.py
# python3 warmup2.py 
# Output: What is todfay's date?Jan. 1, 2000
# Today's date is Jan. 1, 2000
ans=input("What is todfay's date?")
print("Today's date is", ans)

#Warmup3
#git log --oneline 
# 1712bd9 (HEAD -> assignment-2, origin/assignment-2) Warmup1 and 2 completed
# ae854ea (origin/main, origin/HEAD, main) adding homework folder
# 294742d add week 2 folder
# 58d836d Add files via upload
# d8c0c05 Update README.md
# a888c4b Delete week-5/data/.gitkeep
# 06c7f75 Delete week-4/data/.gitkeep
# 202444e Add files via upload
# 677fee9 Add files via upload
# ff7d9dc Add files via upload
# e0ff870 Delete week-7/data/.gitkeep

#Warmup 4 Deliberate error

# print(f"{4+num6}")
#The error message is: NameError: name 'num6' is not defined. This error occurs because the variable num6 has not been defined before it is used in the print statement. To fix this error, you need to define the variable num6 with a value before using it in the print statement.
num6 = 6
print(f"{4+num6}")

#Part 2: Mini-Project
fahr=input("Enter temperature in Fahrenheit: ")
cels=(float(fahr)-32)*5/9
print(f"{float(fahr):.1f} degrees Fahrenheit is {cels:.1f} in Celsius")