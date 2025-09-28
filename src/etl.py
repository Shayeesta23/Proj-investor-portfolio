import pandas as pd, sqlite3, os
os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/portfolio.db")

df = pd.read_csv("data/prices.csv", parse_dates=["date"])
df.to_sql("prices", conn, if_exists="replace", index+False)
conn.close()
print("Loaded prices.csv into SQLite DB (data/portfolio.db)")
