import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('Read data from a csv file...')
data = pd.read_csv("airline-safety.csv")
print(data)

print("How many rows and columns are there?")
print(data.info())

print("Which airline has the most avaialbe seats per week, and how many?")
print(data[data["avail_seat_km_per_week"] == data["avail_seat_km_per_week"].max()][["airline", "avail_seat_km_per_week"]])

print("Top 5 airlines which have the most available seats per week?")
print(data[["airline", "avail_seat_km_per_week"]].sort_values(by="avail_seat_km_per_week", ascending=False).head(5))

print("How many accidents are there?")
print(data.iloc[:, 3:].sum())

print("Top 10 airlines have the most accidents?")
# print(data.iloc[:, 3:].sum(axis=1).sort_values(ascending=False).head(10))
data['totalAcc'] = data.iloc[:, 2:].sum(axis=1)
print(data[["airline", "totalAcc"]].sort_values(by="totalAcc", ascending=False).head(10))

print("Data visualization...")
data2 = data.iloc[:, 2:8].sum()
N = 2
ind = np.arange(N)  # the x locations for the groups
width = 0.2      # the width of the bars

fig, ax = plt.subplots()

incidents = (data2[[0,3]])
incidents_std = (0, 1)
rects1 = ax.bar(ind, incidents, width, color='r', yerr=incidents_std)

fatal_accidents = (data2[[1,4]])
fatal_accidents_std = (3, 5)
rects2 = ax.bar(ind + width, fatal_accidents, width, color='y', yerr=fatal_accidents_std)

fatalities = (data2[[2,5]])
fatalities_std = (3, 5)
rects3 = ax.bar(ind + width *2, fatalities, width, color='g', yerr=fatalities_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Amount')
ax.set_title('Airline Safety')
ax.set_xticks(ind + width)
ax.set_xticklabels(('1985-1999', '2000-2014'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Incidents', 'Fatal-Accidents', 'Fatalities'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.savefig('airline-safety.png')
plt.show()
