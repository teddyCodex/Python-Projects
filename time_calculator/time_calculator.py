def add_time(start, duration):
    pass


days_in_week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]

start = "3:00 PM"
duration = "3:10"

# start = "11:43 PM"
# duration = "24:20"
# day = "tuesday"


def parse_time(start):
    time = start.split()
    hour = int(time[0].split(sep=":")[0])
    mins = int(time[0].split(sep=":")[1])
    time_of_day = time[1]
    return hour, mins, time_of_day


def convert_to_24hrs(hour, time_of_day):
    if time_of_day == "PM":
        hour = hour + 12 if (hour < 12) else hour
    return hour


# parse the start time to extract hour, minutes and time of day
hour, mins, time_of_day = parse_time(start=start)
# convert hour to 24-hour time
hour = convert_to_24hrs(hour=hour, time_of_day=time_of_day)
