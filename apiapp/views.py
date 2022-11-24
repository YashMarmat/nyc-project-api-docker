import requests
from django.shortcuts import render
from .serializers import RideSerializer
from .models import RideModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from apiapp.customFunctions import getDistanceFromLatLon


class RideView(APIView, LimitOffsetPagination):

    def get(self, request):
        rides = RideModel.objects.all()
        paginated_results = self.paginate_queryset(rides, request, view=self)
        serializer = RideSerializer(paginated_results, many=True)
        return self.get_paginated_response(serializer.data)  # json response


def fetchApi(the_api):
    # headers = {'Accept': 'application/json'}
    response = requests.get(the_api)
    return response.json()


class RideDetailView(APIView):

    def get(self, request, pk):
        required_post = RideModel.objects.get(pk=pk)
        serializer = RideSerializer(required_post)
        data_to_send = serializer.data

        weather_api = f"https://api.weather.gov/points/{data_to_send['start_lat']},{data_to_send['start_lng']}/"
        weather_api_response = fetchApi(weather_api)

        weather_forecast_list = fetchApi(
            weather_api_response["properties"]["forecast"])

        stations_list = fetchApi(
            weather_api_response["properties"]["observationStations"])

        data_to_send["weather_information"] = weather_forecast_list["properties"]["periods"]

        record_of_all_stations = stations_list["features"]

        nearest_station_obj = {}

        nearest_value = None

        for each_station in record_of_all_stations:
            station_lat = each_station["geometry"]["coordinates"][1]
            station_long = each_station["geometry"]["coordinates"][0]

            the_distance = getDistanceFromLatLon(
                float(data_to_send['start_lat']),  # beginning of ride
                float(data_to_send['start_lng']),  # beginning of ride
                float(station_lat),
                float(station_long)
            )

            if nearest_value is None:
                nearest_value = the_distance
                nearest_station_obj = each_station
            
            elif the_distance < nearest_value:
                nearest_value = the_distance
                nearest_station_obj = each_station

        data_to_send["stations_information"] = stations_list["features"]
        data_to_send["nearest_station"] = nearest_station_obj

        return Response(data_to_send)
