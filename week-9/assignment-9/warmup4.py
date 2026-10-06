import requests

try:
    res = requests.get("https://thisurldoesnotexist.example.com")
    if res.status_code == 200:
        data = res.json()
    else:
        print(f"Error Status Code: {res.status_code}")
except requests.exceptions.RequestException as err:
    print("Error: Could not reach the server. Check your connection and try again.")
