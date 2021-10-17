#!/usr/bin/python3

# ------- A program to represent the monthly expenses in a pie chart with percentage --------

import matplotlib.pyplot as plt

partitions = ["Holidays", "Eating_Out", "Shopping", "Grocaries"]
sizes = [250, 100, 300, 200]
fig, ax = plt.subplots()
ax.pie(sizes, labels=partitions, autopct="%1.1f%%", shadow=True, startangle=90)
ax.axis("equal")
plt.show()
