def greet(name, greeting="Hiya"):
    return f"{greeting} {name}"

print(greet("Alice"))  # Output: Hiya Alice
print(greet("Bob", "Hello"))  # Output: Hello Bob
print(greet(greeting="Hey", name="Charlie"))  # Output: Hey Charlie