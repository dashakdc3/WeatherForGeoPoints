from folium import Map
from folium.map import Popup
from geo1 import Geo

locations = [[50, 22], [54, 27], [60, 30]]

mymap = Map(location=[54, 27])
# just any point to create a map object instance

for loc in locations:
    geo = Geo(latitude=loc[0], longitude=loc[1])
    geo_weather = geo.weather()
    popup_content = f"""
    Time: {geo_weather[0][0][11:13]} Temp:{geo_weather[0][1]} {geo_weather[0][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[0][3]}@2x.png" width=35>
    <hr style="margin:1px">
    Time: {geo_weather[1][0][11:13]} Temp:{geo_weather[1][1]} {geo_weather[1][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[1][3]}@2x.png" width=35>
    <hr style="margin:1px">
    Time: {geo_weather[2][0][11:13]} Temp: {geo_weather[2][1]} {geo_weather[2][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[2][3]}@2x.png" width=35>
    <hr style="margin:1px">
    Time: {geo_weather[3][0][11:13]} Temp: {geo_weather[3][1]} {geo_weather[3][2]} <img src= "http://openweathermap.org/img/wn/{geo_weather[3][3]}@2x.png" width=35>
    <hr style="margin:1px">
    """

    popup = Popup(popup_content, max_width=400)
    popup.add_to(geo)

    geo.add_to(mymap)

    mymap.save(str("several.html"))
