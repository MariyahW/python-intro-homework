lines=[]
with open("python-intro-homework/week-7/data/notes.txt", 'r') as file:
    for line in file:
        lines.append(line.strip())
for line in lines:
    print(f"Line {lines.index(line)+1}: {line}")