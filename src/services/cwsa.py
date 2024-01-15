# Clarke-Wright Savings Algorithm
from src.utils.distance_functions import get_distance


def calculate_savings(package_list, distance_matrix, hub):
    savings = []
    for i in range(len(package_list)):
        for j in range(i + 1, len(package_list)):
            saving = (get_distance(distance_matrix, hub, package_list[i].address)
                      + get_distance(distance_matrix, hub, package_list[j].address)
                      - get_distance(distance_matrix, package_list[i].address, package_list[j].address))
            savings.append(((package_list[i], package_list[j]), saving))
    return sorted(savings, key=lambda x: x[1], reverse=True)


def combine_routes(savings, package_list):
    # Initialize each package as a separate route
    routes = [[pkg.address] for pkg in package_list]

    for ((package_i, package_j), saving) in savings:
        if saving <= 0:
            continue  # Skip non-beneficial combinations

        # Find the routes that package_i and package_j are currently on
        route_i = next((route for route in routes if package_i.address in route), None)
        route_j = next((route for route in routes if package_j.address in route), None)

        # If both packages are not already on the same route, combine the routes
        if route_i is not None and route_j is not None and route_i != route_j:
            combined_route = route_i + route_j
            routes.remove(route_i)
            routes.remove(route_j)
            routes.append(combined_route)

    return routes
