from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from weatherfor12hours import Weather
from random import uniform
from folium import Map, Marker


class Geo:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.long = longitude

    def round(self):
        return round(float(self.lat), float(self.long))

    def get_time(self):
        x = TimezoneFinder().timezone_at(lat=self.round(), lng=float(self.long))
        return datetime.now(timezone(x))

    def weather(self):
        obj = Weather(api="c07176ef6ccefc38ec63abe1c7085ade",
                      units="metric", lat=float(self.lat), long=(self.long))
        print(obj)
        return obj.next_12_simplified()

    @classmethod
    def random(cls):
        return Geo(
            latitude=uniform(-90, 90),
            longitude=uniform(-180, 180)
        )


y = Geo.random()
weather = y.weather()

rlocation = list((y.lat, y.long))
rmymap = Map(rlocation)

random = Marker(location=rlocation, popup=weather)
random.add_to(rmymap)
rmymap.save(str("random.html"))
