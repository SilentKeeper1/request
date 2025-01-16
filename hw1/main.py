import requests
URL = "https://akabab.github.io/superhero-api/api/all.json"

try:
    response = requests.get(URL)

    if response.status_code == 200:
        heroes = response.json()
        for hero in heroes[:10]:
            print(f"Name: {hero['name']}")
            print(f"Power: {hero['powerstats']}\n")
    else:
        print(f"Помилка: {response.status_code}")
except Exception as e:
    print(f"Виникла помилка: {e}")