from distutils.command.build import build
from floodsystem.geo import stations_by_distance


from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def test_stations_by_distance():
    stations = build_station_list()

    result = stations_by_distance(stations, (0, 0))

    distances = [i[1] for i in result]

    assert len(distances) > 0 and sorted(distances)

test_stations_by_distance()