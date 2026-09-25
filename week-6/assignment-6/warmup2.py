def celToFahr(cel):
    return (cel * 9/5) + 32
def fahrToCel(fahr):
    return (fahr - 32) * 5/9

print(f"0 degrees Celsius is {celToFahr(0)} degrees Fahrenheit")  # Output: 32.0
print(f"32 degrees Fahrenheit is {fahrToCel(32)} degrees Celsius")  # Output: 0.0
print(f"100 degrees Celsius is {celToFahr(100)} degrees Fahrenheit")  # Output: 212.0
print(f"212 degrees Fahrenheit is {fahrToCel(212)} degrees Celsius")  # Output: 100.0