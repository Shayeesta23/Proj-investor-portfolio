import pandas as pd, numpy as np, os
from datetime import datetime, timedelta

os.makedirs("data", exist_ok=True)

dates = pd.date_range("2023-01-01", 2023-12-31")
                      prices = pd.DataFrame( {"data": np.title(dates, 2), "ticker": ["AAPL"]*len(dates) + ["MSFT"]*len(dates),
                                              "price":
                                              list(np.cumsum(np.random.randn(len(dates)))+150 + list(np.cumsum(np.random.randn(len(dates)))+250)
                                                   })
                            prices.to_csv("data/prices.csv", index=False)
                            print("Created data/prices.csv")
