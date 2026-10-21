import requests
import os
from dotenv import load_dotenv

count = 0
load_dotenv()
api_key = os.getenv("API_Key")

try:
    url = "https://api.restcountries.com/countries/v5/region/Europe?response_fields=names.common,population"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    countries = data["data"]["objects"]

    for country in countries:
        if count < 10:
            print(country["names"]["common"])
            count += 1
        else:
            break

except Exception as err:
    print(err)
