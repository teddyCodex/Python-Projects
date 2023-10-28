import requests
from datetime import datetime
from smtplib import SMTP

MY_LAT = 6.550760  # Your latitude
MY_LONG = 3.330900  # Your longitude

SMTPserver = "smtp.gmail.com"
SENDER = "cornwallleveticus@gmail.com"
PASSWORD = "jkxceifgivamfnyv"
DESTINATION = "samted.uche@gmail.com"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# function - Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead(error_margin):
    return (MY_LAT - error_margin) <= iss_latitude <= (MY_LAT + error_margin) and (
        MY_LONG - error_margin
    ) <= iss_longitude <= (MY_LONG + error_margin)


def is_dark():
    return hour_now >= sunset_hour


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.now().hour

# If the ISS is close to my current position
if iss_overhead(error_margin=5) and is_dark():
    message = "Subject: [ISS NOTIFIER] Go Outside and Look up!! \n\nIt's dark outside and The International Space Station is overhead!"
    with SMTP(SMTPserver, 587) as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=DESTINATION,
            msg=message,
        )
