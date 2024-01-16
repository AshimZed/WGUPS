from src.datatypes.status import Status
from src.services.time_from_miles import get_time_from_miles
from src.utils.distance_functions import get_distance
from src.utils.log_event import log_package_event


def update_miles(log_file, day_start, truck, distance_matrix, hub):
    truck.current_mileage += get_distance(distance_matrix, hub, truck.route[0][0])
    time = get_time_from_miles(truck.current_mileage, day_start, truck.speed_mph)
    log_package_event(log_file, time, truck.inv[0], Status.DELIVERED, truck)
    for route in truck.route:
        for idx, ad in enumerate(route):
            if ad != route[-1]:
                truck.current_mileage += get_distance(distance_matrix, ad, route[idx + 1])
                time = get_time_from_miles(truck.current_mileage, day_start, truck.speed_mph)
                log_package_event(log_file, time, truck.inv[idx+1], Status.DELIVERED, truck)

    truck.current_mileage += get_distance(distance_matrix, truck.route[0][-1], hub)
    truck.inv.clear()
