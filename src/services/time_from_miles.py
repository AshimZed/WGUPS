from datetime import timedelta

from src.utils.distance_functions import miles_to_hours


def get_time_from_miles(miles, day_start, truck_speed):

    # print("Input variables are:", miles, day_start, truck_speed)

    time_delta = miles_to_hours(miles, truck_speed)
    # print("Time traveled in hours:", time_delta)

    hours, remainder = divmod(time_delta, 1)
    # print("Hours part of time:", hours)

    minutes = remainder * 60
    # print("Minutes part of time:", minutes)

    # create a time delta object
    delta = timedelta(hours=int(hours), minutes=int(minutes))
    # print("Time delta object:", delta)

    time = day_start + delta
    # print("Final date and time:", time)

    return time
