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


def create():
    print(f"=== Country Explorer ===")
    print(f"1. Search by name")
    print(f"2. Filter by region")
    print(f"3. Quit")
    return input("Choose an option (1-3):")


try:
    url = "https://api.restcountries.com/countries/v5?response_fields=names.common,capitals,region,population"
    api_key = os.getenv("API_Key")
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()["data"]["objects"]

    ans = create()
    while ans != 3:
        match ans:
            case 1:
                searchTermC = input("What is your search term? ").lower()
                countries = searchName(data, searchTermC)
                for country in countries:
                    print(
                        f"{country["country"]} | Capital : {country["capital"]} | Region : {country["region"]} | Population {country["population"]}"
                    )
            case 2:
                searchTermR = input(
                    "What region would you like to search for? "
                ).lower()

                newList = filterRegion(data, searchTermR)
                for country in newList:
                    print(f"{country["name"]}")
            case 3:
                print("Thanks for stopping by!")
            case _:
                print("Invalid entry. Try again. ")
                create()

except Exception as err:
    print(err)
