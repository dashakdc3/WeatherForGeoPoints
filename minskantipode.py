from folium import Map, Marker
from geo import Geo
latitude = float("53.9")
longitude = float("27.6")
geo = Geo(latitude=latitude, longitude=longitude)

antipode_latitude = latitude.__mul__(int("-1"))
if longitude.__le__(float("0")):
    antipode_longitude = longitude.__add__(float("180"))
elif longitude.__gt__(float("180")):
    antipode_longitude = str("invalid longitude")
elif longitude.__gt__(float("0")):
    antipode_longitude = longitude.__sub__(float("180"))

weather = geo.weather()

location1 = list((latitude, longitude))
mymap1 = Map(location1)

minsk = Marker(location=location1, popup=weather)
minsk.add_to(mymap1)
mymap1.save(str("minsk.html"))

location = list((antipode_latitude, antipode_longitude))
mymap = Map(location)
mymap.save(str("antipode.html"))
