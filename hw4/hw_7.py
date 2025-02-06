import requests
import json

def get_popular_anime():
    url = "https://api.jikan.moe/v4/top/anime"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        anime_list = []
        for anime in data.get("data", []):
            anime_list.append({
                "title": anime.get("title"),
                "rating": anime.get("score")
            })
        with open("popular_anime.json", "w", encoding="utf-8") as file:
            json.dump(anime_list, file, ensure_ascii=False, indent=4)
        print("Файл popular_anime.json успішно збережено!")
    else:
        print("Помилка запиту до API:", response.status_code)

get_popular_anime()
