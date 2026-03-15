import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

url = "https://en.wikipedia.org/wiki/List_of_battery_electric_vehicles"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="wikitable")

print("Total tables:", len(tables))

if len(tables) == 0:
    print("No tables found, check HTML")
    exit()

table = tables[0]

rows = table.find_all("tr")

data = []

for row in rows:
    cols = row.find_all("td")

    if len(cols) < 7:
        continue

    model = cols[0].get_text(strip=True)
    year = cols[1].get_text(strip=True)
    body_style = cols[2].get_text(strip=True)
    platform = cols[3].get_text(strip=True)
    bev = cols[4].get_text(strip=True)
    manufacturer = cols[5].get_text(strip=True)
    country = cols[6].get_text(strip=True)

    data.append(
        {
            "model": model,
            "year": year,
            "body_style": body_style,
            "platform": platform,
            "bev": bev,
            "manufacturer": manufacturer,
            "country": country,
        }
    )

print("Rows scraped:", len(data))

df = pd.DataFrame(data)

output_path = Path(__file__).resolve().parent.parent / "data" / "raw_companies.csv"

df.to_csv(output_path, index=False)

print("Saved to", output_path)
