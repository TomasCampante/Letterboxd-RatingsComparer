import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

INPUT_CSV = "ratings.csv"
CACHE_CSV = "all_data.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

#'''
def get_average_rating(letterboxd_url):
    r = requests.get(letterboxd_url, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    tag = soup.find("meta", {"name": "twitter:data2"})
    if tag:
        return float(tag["content"].split()[0])

    return None


# --- load user data ---
df_my = pd.read_csv(INPUT_CSV)

if Path(CACHE_CSV).exists():
    df_cache = pd.read_csv(CACHE_CSV)
else:
    df_cache = pd.DataFrame(columns=[
        "Film",
        "Year",
        "My Rating",
        "Average Rating",
        "Letterboxd URI",
        "Query Date"
    ])

cached_urls = set(df_cache["Letterboxd URI"])

new_rows = []

for _, row in df_my.iterrows():
    film = row["Name"]
    year = row["Year"]
    my_rating = row["Rating"]
    url = row["Letterboxd URI"]

    if url in cached_urls:
        continue

    avg_rating = get_average_rating(url)
    query_date = datetime.now().strftime("%Y-%m-%d")

    print(f"{film}, {my_rating}, {avg_rating}")

    new_rows.append({
        "Film": film,
        "Year": year,
        "My Rating": my_rating,
        "Average Rating": avg_rating,
        "Letterboxd URI": url,
        "Query Date": query_date
    })

    time.sleep(.1)  # respect the website (and its servers)


# --- save cache ---
if new_rows:
    df_new = pd.DataFrame(new_rows)
    df_cache = pd.concat([df_cache, df_new], ignore_index=True)
    df_cache.to_csv(CACHE_CSV, index=False)

#'''

# --- load cache (aka: all data) ---
df = pd.read_csv(CACHE_CSV)

# ensure valid data
df = df.dropna(subset=["My Rating", "Average Rating"])

# --- plot ---
plt.figure()
plt.scatter(df["My Rating"],df["Average Rating"],s=1,marker='o', alpha=0.7, label='Data')

plt.ylabel("Average rating (Letterboxd)")
plt.xlabel("My rating")

plt.plot([0, 5], [0, 5], color='black',linewidth=.5, linestyle='--', label='Perfect correspondence')  # linha identidade
plt.xlim(0,5.5)
plt.ylim(0,5)
plt.gca().set_aspect("equal", adjustable="box")
plt.show()
