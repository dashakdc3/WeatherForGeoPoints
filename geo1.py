from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from weatherfor12hours import Weather
from random import uniform
from folium import Marker


class Geo(Marker):
    def __init__(self, latitude, longitude, popup=None):
        super().__init__(location=[latitude, longitude], popup=popup)
        self.lat = latitude
        self.long = longitude
        self.popup = popup

    def round(self):
        return round(float(self.lat))

    def get_time(self):
        x = TimezoneFinder().timezone_at(lat=self.round(), lng=float(self.long))
        return datetime.now(timezone(x))

    def weather(self):
        obj = Weather(api="c07176ef6ccefc38ec63abe1c7085ade",
                      units="metric", lat=float(self.lat), long=(self.long))
        return obj.next_12_simplified()

    @classmethod
    def random(cls):
        return Geo(
            latitude=uniform(-90, 90),
            longitude=uniform(-180, 180)
        )


if __name__ == "__main__":
    y = Geo.random()
    print(y.weather())
