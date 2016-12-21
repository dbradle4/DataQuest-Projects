import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
sphist = pd.read_csv("sphist.csv")
sphist["Date"] = pd.to_datetime(sphist["Date"])
from datetime import datetime
sphist = sphist.sort_values(by="Date", ascending=True)

def Last_5(row):
    i=int(row.name)
    if i >= 5:
        start = i-5
        end = i-1
        mean = sphist.iloc[start:end]["Close"].mean()
        return mean
    else:
        return 0
sphist["Last 5 Avg"] = sphist.apply(lambda row: Last_5(row), axis=1)

def Last_365(row):
    i=int(row.name)
    if i >= 365:
        start = i-365
        end = i-1
        mean = sphist.iloc[start:end]["Close"].mean()
        return mean
    else:
        return 0
sphist["Last 365 Avg"] = sphist.apply(lambda row: Last_365(row), axis=1)

def Ratio_365_5(row):
    if row["Last 5 Avg"] != 0:
        ratio = row["Last 365 Avg"]/row["Last 5 Avg"]
        return ratio
    else:
        return 0
sphist["Ratio 365/5"] = sphist.apply(lambda row: Ratio_365_5(row), axis=1)

def volume_stdev_5days(row):
    i = int(row.name)
    if i >=5:
        start = i-5
        end = i-1
        std = np.std(sphist.iloc[start:end]["Volume"])
        return std
    else:
        return 0
sphist["Stdev Vol Last 5"] = sphist.apply(lambda row: volume_stdev_5days(row), axis=1)

def volume_stdev_365days(row):
    i = int(row.name)
    if i >=365:
        start = i-365
        end = i-1
        std = np.std(sphist.iloc[start:end]["Volume"])
        return std
    else:
        return 0
sphist["Stdev Vol Last 365"] = sphist.apply(lambda row: volume_stdev_365days(row), axis=1)

sphist = sphist[sphist["Date"] > datetime(year=1951, month=1, day=2)]
sphist = sphist.dropna(axis=0)

train = sphist[sphist["Date"] < datetime(year=2013, month=1, day=1)]
test = sphist[sphist["Date"] >= datetime(year=2013, month=1, day=1)]
lr = LinearRegression()
lr.fit(train[["Last 5 Avg", "Last 365 Avg", "Ratio 365/5", "Stdev Vol Last 5", "Stdev Vol Last 365"]], train["Close"])
predictions = lr.predict(test[["Last 5 Avg", "Last 365 Avg", "Ratio 365/5", "Stdev Vol Last 5", "Stdev Vol Last 365"]])

mae = mean_absolute_error(test["Close"], predictions)
print(mae)