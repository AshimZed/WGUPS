from src.utils.distance_functions import get_distance


def update_miles(truck, hub, distance_matrix):
    truck.current_mileage += get_distance(distance_matrix, hub, truck.route[0][0])
    for route in truck.route:
        for idx, ad in enumerate(route):
            if ad != route[-1]:
                truck.current_mileage += get_distance(distance_matrix, ad, route[idx + 1])
            else:
                truck.current_mileage += get_distance(distance_matrix, ad, hub)
    truck.inv.clear()
