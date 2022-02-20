from re import S
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt


stations = build_station_list()

#Update data
update_water_levels(stations)

#returns top 5 greatest water level stations
at_risk_stations = stations_highest_rel_level(stations, 5)


#water level the past 2 days
dt = 2
for s in at_risk_stations:
    dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))

    #original data points
    plt.plot(dates, levels, '.')

    #polynomial fit
    plot_water_level_with_fit(s, dates, levels, 4)

    #Typical High Low Range
    high = []
    low = []
    for i in dates:
        high.append(s.typical_range[1])
        low.append(s.typical_range[0])
    plt.plot(dates, low, label = "Typical Low")
    plt.plot(dates, high, label = "Typical High")

    plt.show()
    
