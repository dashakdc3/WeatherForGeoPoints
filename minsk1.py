from folium import Map
from folium.map import Popup
from geo1 import Geo

latitude = float("54")
longitude = float("27")
# locations = [[42, -1], [40, 2], [39, 5]]

mymap = Map(location=[latitude, longitude])

# geo = Geo(latitude=latitude, longitude=longitude, popup="hei")
# popup = Popup(str(geo.weather()))
# popup.add_to(geo)

geo = Geo(latitude=latitude, longitude=longitude)
geo_weather = geo.weather()
print(geo_weather)
popup_content = f"""
{geo_weather[0][0][11:13]} {geo_weather[0][1]} {geo_weather[0][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[0][3]}@2x.png" width=35>
<hr style="margin:1px">
{geo_weather[1][0][11:13]} {geo_weather[1][1]} {geo_weather[1][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[1][3]}@2x.png" width=35>
<hr style="margin:1px">
{geo_weather[2][0][11:13]} {geo_weather[2][1]} {geo_weather[2][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[2][3]}@2x.png" width=35>
<hr style="margin:1px">
{geo_weather[3][0][11:13]} {geo_weather[3][1]} {geo_weather[3][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[3][3]}@2x.png" width=35>
<hr style="margin:1px">
"""


popup = Popup(popup_content, max_width=400)
popup.add_to(geo)
geo.add_to(mymap)
mymap.save(str("minsk1.html"))

# mymap = Map(location=[latitude, longitude])
# =
# location1 = list((latitude, longitude))
# mymap1 = Map(location1)


# print(dir(folium))
# NOTE: Popup is a class, not only an attribute of Marker class

# print(dir(folium.Popup))
# also has add_to method.
