import geopy

def get_address(latitude, longitude):
    geolocator = geopy.geocoders.Nominatim(user_agent="weather_bot")
    location = geolocator.reverse((latitude, longitude), language='ru')
    if location is not None:
        return location.address
    else:
        return "Адрес не найден"