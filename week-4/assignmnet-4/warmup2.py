student={"name":"John",
         "grade":10,
         "courses":["Math","Science","History"]}

for key,value in student.items():
    print(f"{key}:{value}")

student["graduated"]=False

print(student)