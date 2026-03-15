import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

raw_path = base_path / "data" / "raw_companies.csv"
clean_path = base_path / "data" / "cleaned_companies.csv"

df = pd.read_csv(raw_path)

print("Original rows:", len(df))

# remove duplicates
df = df.drop_duplicates()

# remove empty manufacturer rows
df = df.dropna(subset=["manufacturer"])

# strip spaces
df["manufacturer"] = df["manufacturer"].str.strip()
df["country"] = df["country"].str.strip()

print("After cleaning:", len(df))

df.to_csv(clean_path, index=False)

print("Saved cleaned file")

company_df = (
    df.groupby(["manufacturer", "country"]).size().reset_index(name="number_of_models")
)

company_df["industry"] = "Electric Vehicles"

company_path = base_path / "data" / "company_intelligence.csv"

company_df.to_csv(company_path, index=False)

print("Saved company intelligence dataset")
