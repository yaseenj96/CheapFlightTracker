import requests
import datetime as dt

today = dt.date.today()
departDate = today + dt.timedelta(60)

API_KEY = '8347abe1c8msh32c4f43585a917fp1d3bcbjsn6952df846a15'
API_HOST = 'sky-scanner3.p.rapidapi.com'


url = "https://sky-scanner3.p.rapidapi.com/flights/cheapest-one-way"


headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": API_HOST
}

# params = {"fromEntityId": "ORD", "toEntityId": "JFK", "departDate": departDate}
# response = requests.get(url, headers=headers, params=params)
# print(response)
# print(response.status_code)
# print(response.json()["data"][0]["price"])

class FlightSearch:
    def get_destination_code(self, city_name):
        code = "testing"
        return code

    def get_cheapest_flight(self, iata_code):
        params = {"fromEntityId": "ORD", "toEntityId": iata_code, "departDate": departDate}
        response = requests.get(url, headers=headers, params=params)
        return response.json()["data"][0]["price"]

