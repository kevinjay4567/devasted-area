from django.http import HttpResponse
import http.client
import json


def index():
    return HttpResponse("<h1>Hello world</h1>")


def catastrofe_detector(lat, lon):
        conn = http.client.HTTPSConnection("ai-weather-by-meteosource.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "92be4df953msh2902bee9f779884p1fa4ebjsn28c2a8842961",
            'X-RapidAPI-Host': "ai-weather-by-meteosource.p.rapidapi.com"
        }

        conn.request("GET", f"/current?lat={lat}&lon={lon}&timezone=auto&language=es&units=auto", headers=headers)
        res = conn.getresponse()
        data = res.read()
        wether_data = json.loads(data.decode('utf-8'))
        timezone = wether_data['timezone']
        current = wether_data['current']
        temperature = current['temperature']
        summary = current['summary']
        precipitation = current['precipitation']['type']
        wind = current['wind']['speed']
        return [timezone, temperature, summary, precipitation, wind]