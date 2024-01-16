from src.services.cwsa import calculate_savings, combine_routes


def optimize_route(truck, distance_matrix, hub):
    truck_savings = calculate_savings(truck.inv, distance_matrix, hub)
    truck.route = combine_routes(truck_savings, truck.inv)
