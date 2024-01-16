from datetime import datetime
from pathlib import Path

from src.datatypes.address import Address
from src.datatypes.truck import Truck
from src.services.optimize_route import optimize_route
from src.services.package_loader import package_loader
from src.services.pkg_pool import update_pkg_pool
from src.services.print_route import print_route
from src.services.time_from_miles import get_time_from_miles
from src.services.truck_loader import load_trucks
from src.services.update_links import update_links
from src.services.update_miles import update_miles
from src.utils.csv_parser import read_csv
from src.utils.initialize_log_file import initialize_log_file


def bootstrap():
    while True:
        base_path = Path.cwd()

        # Create log file
        log_file_path = base_path / 'data/package_log.csv'
        headers = ['timestamp', 'package_id', 'status', 'truck_id']
        initialize_log_file(log_file_path, headers)

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

        # Day Start
        day_start = datetime.strptime("8:00 am", '%I:%M %p')
        hub = addresses[0]

        # Load packages at the start of the day
        packages = package_loader(addresses, packages_file, trucks, "8:00 am", log_file_path)
        packages_set = set()
        for key, package in packages:
            packages_set.add(package)
        update_links(packages_set)

        # Load package pool
        package_history = set()
        depot, package_history = update_pkg_pool(log_file_path, packages_set, day_start, package_history)

        loop_counter = 0
        change_flag = True
        while len(package_history) < len(packages_set):
            # print(f"Entering while loop iteration: {loop_counter}\n"
            #       f"Packages Delivered: {len(package_history)}\tPackages Available: {len(depot)}"
            #       f"\tTotal Packages: {len(packages_set)}")
            min_miles_truck = trucks[0]
            for truck in trucks:
                if truck.current_mileage < min_miles_truck.current_mileage:
                    min_miles_truck = truck

            if change_flag:
                time = get_time_from_miles(min_miles_truck.current_mileage, day_start, min_miles_truck.speed_mph)
                depot, package_history = update_pkg_pool(log_file_path, packages_set, time, package_history)
            else:
                time = get_time_from_miles((min_miles_truck.current_mileage + loop_counter),
                                           day_start, min_miles_truck.speed_mph)
                depot, package_history = update_pkg_pool(log_file_path, packages_set, time, package_history)

            # print(f"Loading truck: {min_miles_truck.truck_id}")
            depot, package_history, [min_miles_truck] = load_trucks(log_file_path, time, depot,
                                                                    package_history, [min_miles_truck])
            if not min_miles_truck.inv:
                change_flag = False
                loop_counter += 1
                continue

            optimize_route(min_miles_truck, distance_matrix, hub)
            # print_route(min_miles_truck, distance_matrix, hub)
            update_miles(log_file_path, day_start, min_miles_truck, distance_matrix, hub)

        total_miles = 0
        for truck in trucks:
            total_miles += truck.current_mileage
        # print(f"Total Miles: {total_miles}")
        if total_miles <= 140:
            break

    # for truck in trucks:
    #     print(f"Truck: {truck.truck_id}\tMileage: {truck.current_mileage}")

    return trucks, packages_set
