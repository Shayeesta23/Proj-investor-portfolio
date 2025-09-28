import streamlit as st, pandas as pd, sqlite3

st.title("Investor Portfolio Dashboard")

conn = sqlite3.connect("data/portfolio.db")
df = pd.read_sql("SELECT * FROM prices", conn, parse_dates=["date"])
conn.close()

st.line_chart(df.pivot(index="date", columns="ticker", values="price"))
st.write(df.head())
