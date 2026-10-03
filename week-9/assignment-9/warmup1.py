import requests

res = requests.get("https://api.agify.io/?name=michael")
print(f"Status code: {res.status_code}")
print(f"Response: {res.json()}")
