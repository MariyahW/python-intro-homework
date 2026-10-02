def greet(name, greeting="Hello"):
    return f"{greeting} {name}"


print(greet("Alice"))  # Output: Hello Alice
print(greet("Bob", "Hiya"))  # Output: Hiya Bob
print(greet(greeting="Hey", name="Charlie"))  # Output: Hey Charlie
