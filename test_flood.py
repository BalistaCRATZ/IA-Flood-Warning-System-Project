from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():

    threshold_stations = stations_level_over_threshold(stations, 0.4)

    for s in threshold_stations:
        assert s[1] is not None and s[1] > 0.4

def test_stations_highest_rel_level():

    highest_stations = stations_highest_rel_level(stations, 30)

    h = []
    for i in highest_stations:
        assert i.relative_water_level is not None
        h.append(i.relative_water_level())

    assert sorted(reversed(h)) and len(h) == 30