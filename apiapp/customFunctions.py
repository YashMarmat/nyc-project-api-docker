import pytz
import datetime
import math


def modifyDate(date_received):

    # customize dates
    custom_date = date_received.split(" ")
    the_date = custom_date[0].split("-")[0]
    the_month = custom_date[0].split("-")[1]
    the_year = custom_date[0].split("-")[2]

    custom_date = custom_date[1]

    date_hours = custom_date.split(":")[0]
    date_mins = custom_date.split(":")[1]

    # according to django DecimalField
    new_customized_date = datetime.datetime(
        int(the_year),
        int(the_month),
        int(the_date),
        int(date_hours),
        int(date_mins),
        0,
        tzinfo=pytz.timezone('UTC')
    )

    return new_customized_date


def getDistanceFromLatLon(lat1, lon1, lat2, lon2):

    # print("===>", lat1, lon1, lat2, lon2)

    """
    Based on Haversine formula

    Requires four parameters:

    1. User Current Latitude (beginning of ride),
    2. User Current Longitude (begining of ride),
    3. Some other station Latitude
    4. Some other station Longitude
    """

    R = 6371  # Radius of the earth in km
    dLat = deg2rad(lat2-lat1)  # deg2rad below
    dLon = deg2rad(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * \
        math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c  # Distance in km

    return d


def deg2rad(deg):
    return deg * (math.pi/180)
