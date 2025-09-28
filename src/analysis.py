import sqlite3, pandas as pd, os 

os.makedirs("outputs", exist_ok=True)

conn = sqlite3.connect("data/portfolio.db")
df = pd.read_sql("SELECT * FROM prices", conn, parse_dates=["date"])
conn.close()

# Simple daily return
df["return"] = df.groupby("ticker")["price"].pct_change()
df.to_excel("outputs/portfolio_report.xlsx", index=False)

print("Analysis complete. See outputs/portfolio_report.xlsx")
