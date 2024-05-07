import requests
import smtplib

my_email = "yj96throwaway@gmail.com"
password = "eanq qemm bevo zsls"

sheety_api = 'https://api.sheety.co/ff51a3baae42f20474c74cb805766a6c/flightDeals/prices'
sheety_api_user = 'https://api.sheety.co/ff51a3baae42f20474c74cb805766a6c/flightDeals/users'

class NotificationManager:
    def __init__(self):
        self.destination_data = {}
        self.emails = {}

    def send_emails(self):
        sheet_data = requests.get(url=sheety_api).json()
        sheet_data2 = requests.get(url=sheety_api_user).json()
        self.destination_data = sheet_data["prices"]
        self.emails = sheet_data2["users"]

        content = "Here are the latest flight deals!\n"
        for destination in self.destination_data:
            if destination["lowestFlightPrice"] < destination["lowestPrice"]:
                content = content + f"Fly to {destination["city"]} for ${destination["lowestFlightPrice"]}!\n"

        for email in self.emails:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email["email"],
                                     msg=f"Subject:New Flight Deal!\n\n{content}")


