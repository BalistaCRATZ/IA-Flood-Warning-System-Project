from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
import matplotlib

stations = build_station_list()
update_water_levels(stations)

low_stations = []
moderate_stations = []
high_or_severe_stations = []
high_stations = []
severe_stations = []

#If the relative water level of a station is below 1.5, it should be classed as either moderate or low risk of flooding
for s in stations:
    if s.relative_water_level() is not None:
        if s.relative_water_level() <= 1.5 and s.relative_water_level() > 1:
            moderate_stations.append(s)
        elif s.relative_water_level() <= 1:
            low_stations.append(s)
        elif s.relative_water_level() >= 1.5:
            high_or_severe_stations.append(s)

    else:
        pass


#returns top 5 greatest water level stations
dt = 2
p = 4

for s in high_or_severe_stations:
    dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))
    x = matplotlib.dates.date2num(dates)
    #shifting of the date axis
    p_coeff =np.polyfit(x-x[0], levels, p)

    poly = np.poly1d(p_coeff)
    #print(poly)
    #print(poly.deriv())
    #print(x[-1])
    gradient = np.polyval(poly, x[-1])
    if gradient >0:
        severe_stations.append(s)
    elif gradient <= 0 :
        high_stations.append(s)


print(len(high_stations))
print(len(severe_stations))
print(len(low_stations))
print(len(moderate_stations))

