import requests
import os
from pprint import pprint

sheety_api = 'https://api.sheety.co/ff51a3baae42f20474c74cb805766a6c/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_data = requests.get(url=sheety_api).json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {
                        "iataCode": city["iataCode"]
                    }
            }
            response = requests.put(
                url= f"{sheety_api}/{city['id']}",
                json=new_data
            )

            print(response.text)

    def update_lowest_price(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {
                        "lowestFlightPrice": city["lowestFlightPrice"]
                    }
            }
            response = requests.put(
                url= f"{sheety_api}/{city['id']}",
                json=new_data
            )
            print(response.text)
    #This class is responsible for talking to the Google Sheet.
