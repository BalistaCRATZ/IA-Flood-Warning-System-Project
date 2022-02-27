import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from re import S
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta

def test_polyfit():
    stations = build_station_list()
    at_risk_stations = stations_highest_rel_level(stations, 5)
    for s in at_risk_stations:
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))
        result = polyfit(dates, levels, 2)

        assert type(result) == list and len(result) >= 0

test_polyfit()