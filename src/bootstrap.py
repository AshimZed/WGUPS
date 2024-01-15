from datetime import datetime
from pathlib import Path

from src.datatypes.address import Address
from src.datatypes.truck import Truck
from src.services.cwsa import calculate_savings, combine_routes
from src.services.package_loader import package_loader
from src.services.pkg_pool import update_pkg_pool
from src.services.truck_loader import load_trucks
from src.services.update_links import update_links
from src.utils.csv_parser import read_csv
from src.utils.distance_functions import get_distance


def bootstrap():
    base_path = Path.cwd()

    # Assign data file locations
    packages_file = base_path / "data/package_data.csv"
    address_file = base_path / "data/address_file.csv"
    distance_file = base_path / "data/distance_data.csv"

    # Instantiate databases
    addresses = []
    distance_matrix = []

    # Parse addresses csv file and store in a list
    data = read_csv(address_file)
    for row in data:
        index = int(row[0])
        name = row[1]
        address = row[2]
        addresses.append(Address(index, name, address))

    # Parse distance matrix csv and store in a 2D list
    data = read_csv(distance_file)
    for row in data:
        distance_matrix.append(row)
    distance_matrix = [[float(cell) if cell else None for cell in row] for row in distance_matrix]

    # Instantiate two trucks from the assignment
    truck_1 = Truck(1)
    truck_2 = Truck(2)
    trucks = [truck_1, truck_2]
    minimum_speed = min([truck.speed_mph for truck in trucks])
    maximum_capacity = min([truck.max_inv for truck in trucks])

    # Day Start
    day_start = datetime.strptime("8:00 am", '%I:%M %p')
    hub = addresses[0]

    # Load packages at the start of the day
    packages = package_loader(addresses, packages_file, trucks, "8:00 am")
    packages_set = set()
    for key, package in packages:
        packages_set.add(package)
    update_links(packages_set)

    # Load package pool
    package_history = set()
    depot = update_pkg_pool(packages_set, day_start, package_history)

    # Load truck loads
    load_trucks(depot, trucks)
    for truck in trucks:
        for package in truck.inv:
            package_history.add(package.package_id)
