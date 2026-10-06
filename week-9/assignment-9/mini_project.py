import requests
import os
from dotenv import load_dotenv

option = ""


def searchName(countries, term):
    list = []
    for country in countries:
        try:
            if term in country["names"]["official"].lower():
                list.append(
                    {
                        "country": country["names"]["official"],
                        "capital": country["capital"]["name"],
                        "region": country["region"],
                        "population": country["population"],
                    }
                )
        except KeyError as key:
            print(key)

    return list


def filterRegion(countries, term):
    list = []
    for country in countries:
        if term == country["region"].lower():
            list.append(
                {
                    "name": country["names"]["official"],
                    "population": int(country["population"]),
                }
            )
    sorted_list = sorted(list, key=lambda x: x["population"], reverse=True)
    return sorted_list


try:
    url = "https://api.restcountries.com/countries/v5?response_fields=names.common,capitals,region,population"
    api_key = os.getenv("API_Key")
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()["data"]["objects"]
    option = input("")

except Exception as err:
    print(err)
