from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number, stations_by_distance, stations_within_radius, rivers_with_station, station_by_river

stations = build_station_list()

def test_stations_by_distance():
    result = stations_by_distance(stations, (0, 0))

    distances = [i[1] for i in result]

    assert len(distances) > 0 and sorted(distances)

def test_stations_within_radius():
    result = stations_within_radius(stations, (52.2053, 0.1218), 5)
    
    assert len(result) == 3

def test_rivers_with_station():
    
    result = rivers_with_station(stations)

    assert result.__contains__(None) == False

def test_station_by_river():
    
    result = station_by_river(stations)

    assert result['Arkle Beck'][0].name == 'Reeth'

def test_rivers_by_station_number():
    
    result = rivers_by_station_number(stations, 13)
#to show that the programm will print stations with equal number of the staions as the Nth entry
    assert len(result) == 14