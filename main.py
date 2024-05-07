#This file will need to use the DataManager,FlightSearch, FightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from pprint import pprint

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

print(sheet_data)


from flight_search import FlightSearch
flight_search = FlightSearch()
for row in sheet_data:
    print(row["iataCode"])
    row["lowestFlightPrice"] = flight_search.get_cheapest_flight(row["iataCode"])
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_lowest_price()

from notification_manager import NotificationManager
notification_manager = NotificationManager()
notification_manager.send_emails()