import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
def plot_water_levels(station, dates, levels):
    #plot
    plt.plot(dates, levels, label = "Water Level")
    high = []
    low = []
    for i in dates:
        high.append(station.typical_range[1])
        low.append(station.typical_range[0])
    plt.plot(dates, low, label = "Typical Low")
    plt.plot(dates, high, label = "Typical High")

    #Add axis
    plt.xlabel("Date")
    plt.ylabel("Water Level(m)")
    plt.title(station.name)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

