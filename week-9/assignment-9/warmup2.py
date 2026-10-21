import requests

try:
    res = requests.get("https://api.agify.io/?name=michael")
    data = res.json()

    print(data)
    # Using standard dictionary brackets for keys we know exist
    print(f"Name: {data['name']}")
    print(f"Predicted Age: {data['age']}")

    # Using .get() for keys that might be missing, with a fallback
    print(f"Birthday : {data.get('birthday', 'Not available')}")

except Exception as err:
    print(err)
