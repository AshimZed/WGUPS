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
    # Initialize a parallel list for packages in order
    ordered_packages = [[pkg] for pkg in package_list]

    for ((package_i, package_j), saving) in savings:
        if saving <= 0:
            continue  # Skip non-beneficial combinations

        # Find the routes and package lists that package_i and package_j are currently on
        route_i_index = next((i for i, route in enumerate(routes) if package_i.address in route), None)
        route_j_index = next((i for i, route in enumerate(routes) if package_j.address in route), None)

        if route_i_index is not None and route_j_index is not None and route_i_index != route_j_index:
            # Combine the routes
            routes[route_i_index] += routes[route_j_index]
            del routes[route_j_index]
            # Combine the corresponding package lists
            ordered_packages[route_i_index] += ordered_packages[route_j_index]
            del ordered_packages[route_j_index]

    return routes, [pkg for sublist in ordered_packages for pkg in sublist]
