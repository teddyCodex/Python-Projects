HOURS_IN_DAY = 24
HALF_DAY = 12
MINS_IN_HOUR = 60
MINS_IN_DAY = HOURS_IN_DAY * MINS_IN_HOUR


def add_time(start, duration, day=None):
    days_in_week = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]

    def parse_time(time) -> tuple:
        """
        Accepts a list with time info as a string.
        Returns the hour and minute of that time in an integer tuple (hour, min).
        Also returns time of day if that value is present.
        """
        if len(time) > 1:
            hour = int(time[0].split(sep=":")[0])
            mins = int(time[0].split(sep=":")[1])
            time_of_day = time[1]
            return hour, mins, time_of_day
        else:
            time = time[0].split(sep=":")
            hour = int(time[0])
            mins = int(time[1])
            return hour, mins

    def convert_to_24hrs(time) -> int:
        """
        Accepts an integer and returns the equivalent
        value in 24 hr time
        """
        return time + HALF_DAY

    def convert_to_mins(start_hour, start_mins, duration_hours, duration_mins) -> tuple:
        """
        Accepts only integers and returns a tuple of integers
        """
        start_in_mins = (start_hour * MINS_IN_HOUR) + start_mins
        duration_in_mins = (duration_hours * MINS_IN_HOUR) + duration_mins
        return start_in_mins, duration_in_mins

    def format_output(current_time, days_passed=0, day=None):
        """
        Accepts one required argument and two optional
        Formats the output accordingly depending on provided arguments
        """
        if day:
            day = day.title()
        if days_passed == 1 and day:
            output = f"{current_time}, {day} (next day)"
        elif days_passed > 1 and day:
            output = f"{current_time}, {day} ({days_passed} days later)"
        elif day:
            output = f"{current_time}, {day}"
        elif days_passed == 1:
            output = f"{current_time} (next day)"
        elif days_passed > 1:
            output = f"{current_time} ({days_passed} days later)"
        else:
            output = current_time

        return output

    # parse the start time and duration to extract hour, minutes and time of day
    start, duration = start.split(), duration.split()
    start_hour, start_mins, time_of_day = parse_time(time=start)
    duration_hours, duration_mins = parse_time(time=duration)
    # convert start_hour to 24hrs time
    if time_of_day == "PM":
        start_hour = convert_to_24hrs(start_hour)

    # convert all time to mins
    start_in_mins, duration_in_mins = convert_to_mins(
        start_hour=start_hour,
        start_mins=start_mins,
        duration_hours=duration_hours,
        duration_mins=duration_mins,
    )

    # factor in duration calculate the current time
    total_minutes = start_in_mins + duration_in_mins
    current_hour = total_minutes // MINS_IN_HOUR
    current_mins = total_minutes - (current_hour * MINS_IN_HOUR)
    days_passed = total_minutes // MINS_IN_DAY

    # make sure current hour is in 24hr time
    while current_hour > HOURS_IN_DAY:
        current_hour -= HOURS_IN_DAY

    # check if current hour is midnight and convert to 12hr time
    if current_hour == HOURS_IN_DAY:
        current_hour = HALF_DAY

    # add a zero if minutes is a single digit
    if current_mins < 10:
        current_mins = f"0{current_mins}"

    # format time string without day and days passed
    if days_passed == 0 and current_hour == HALF_DAY:
        current_time = f"{current_hour}:{current_mins} PM"
    elif current_hour <= HALF_DAY:
        current_time = f"{current_hour}:{current_mins} AM"
    else:
        current_hour -= HALF_DAY
        current_time = f"{current_hour}:{current_mins} PM"

    current_day = None

    # if day is provided, format accordingly
    if day:
        day_index = days_in_week.index(day.lower())
        current_day_index = day_index + days_passed
        while current_day_index > (len(days_in_week) - 1):
            current_day_index -= len(days_in_week)
        current_day = days_in_week[current_day_index]

    return format_output(current_time, days_passed, current_day)
