import pandas as pd

print('Read data from a csv file...')
data = pd.read_csv("airline-safety.csv")

print("How many rows and columns are there?")
print(data.info())

print("Which airline has the most avaialbe seats per week, and how many?")
print(data[data["avail_seat_km_per_week"] == data["avail_seat_km_per_week"].max()][["airline", "avail_seat_km_per_week"]])

print("Top 5 airlines which have the most available seats per week?")
print(data[["airline", "avail_seat_km_per_week"]].sort_values(by="avail_seat_km_per_week", ascending=False).head(5))

print("How many accidents are there?")
print(data.iloc[:, 3:].sum())

print("Top 10 airlines have the most accidents?")
print(data.iloc[:, 3:].sum(axis=1).sort_values(ascending=False).head(10))
data['totalAcc'] = sort_values(ascending=False).head(10)
print(data[["airline", "totalAcc"]].sort_values(by="totalAcc", ascending=False).head(10))