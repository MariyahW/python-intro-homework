import requests

try:
    res = requests.get("https://api.agify.io/?name=michael")
    data = res.json()
    reset = res.headers.get("X-Rate-Limit-Reset")
    print(reset)
    try:
        print(data)
        print(f"Name: {data["name"]}")
        print(f"Predicted Age: {data["age"]}")
        print(f"Birthday : {data["birthday"]}")
    except Exception as err:
        print(err)
except Exception as err:
    print(err)
