def celsius_to_fahrenheit(cel):
    return (cel * 9 / 5) + 32


def fahrenheit_to_celsius(fahr):
    return (fahr - 32) * 5 / 9


print(
    f"0 degrees Celsius is {celsius_to_fahrenheit(0)} degrees Fahrenheit"
)  # Output: 32.0
print(
    f"32 degrees Fahrenheit is {fahrenheit_to_celsius(32)} degrees Celsius"
)  # Output: 0.0
print(
    f"100 degrees Celsius is {celsius_to_fahrenheit(100)} degrees Fahrenheit"
)  # Output: 212.0
print(
    f"212 degrees Fahrenheit is {fahrenheit_to_celsius(212)} degrees Celsius"
)  # Output: 100.0
