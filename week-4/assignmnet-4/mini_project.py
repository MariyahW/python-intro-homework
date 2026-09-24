students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
top=0
name=""
avg=0
cumulative=0
setCourses=set()
topStudents=[]
for student in students:
    if student["score"]>top:
        top=student["score"]
        name=student["name"]
    if student["score"]>75:
        topStudents.append(student["name"])
    cumulative+=student["score"]
    setCourses.add(student["subject"])
avg=cumulative/len(students)
print(f"Top Student: {name} with score {top}")
print(f"Average Score: {avg}")
print(f"Top Students: {topStudents}")
print(f"Courses: {setCourses}")
