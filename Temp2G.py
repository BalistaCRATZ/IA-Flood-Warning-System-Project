from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime
import numpy as np
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()

#Update data
update_water_levels(stations)

#returns top 5 greatest water level stations
at_risk_stations = stations_highest_rel_level(stations, 5)
dt = 2
p = 4
def derivative():
    for s in stations:
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))
        x = matplotlib.dates.date2num(dates)\
        #shifting of the date axis
        p_coeff =np.polyfit(x-x[0], levels, p)

        poly = np.poly1d(p_coeff)
        print(poly)
        print(poly.deriv())
        print(x[-1])
        gradient = np.polyval(poly, x[-1])
        print(gradient)



derivative()



