from src.utils.distance_functions import get_distance


def print_route(truck, distance_matrix, hub):
    print(f"Truck {truck.truck_id} Route: ")
    print(f"{hub} --{get_distance(distance_matrix, hub, truck.route[0][0])}-->")

    idx = 0
    while truck.route[0][-1] != truck.route[0][idx]:
        print(f"{truck.route[0][idx]} --"
              f"{get_distance(distance_matrix, truck.route[0][idx], truck.route[0][idx+1])}-->")
        idx += 1
    print(f"{truck.route[0][-1]} --{get_distance(distance_matrix, truck.route[0][-1], hub)}-->")
    print(f"{hub} ---Route Finished---")
