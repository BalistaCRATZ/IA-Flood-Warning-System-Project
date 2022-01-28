from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()

#Co-ordinates of Cambridge city centre
p = (52.2053, 0.1218)

x = stations_by_distance(stations, p)

#Formatting result into form (city name, town, distance)
formatted_x = []
for i in x:
    formatted_x.append((i[0].name, i[0].town, i[1]))

print(f"Closest 10: {formatted_x[:10]}")
print(f"Furthest 10: {formatted_x[-10:]}")
