# .----------------------------------------------------------------------------------------------------------.
# |__/\\\______________/\\\_____/\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\\\_______/\\\\\\\\\\\___        |
# | _\/\\\_____________\/\\\___/\\\//////////__\/\\\_______\/\\\_\/\\\/////////\\\___/\\\/////////\\\_       |
# |  _\/\\\_____________\/\\\__/\\\_____________\/\\\_______\/\\\_\/\\\_______\/\\\__\//\\\______\///__      |
# |   _\//\\\____/\\\____/\\\__\/\\\____/\\\\\\\_\/\\\_______\/\\\_\/\\\\\\\\\\\\\/____\////\\\_________     |
# |    __\//\\\__/\\\\\__/\\\___\/\\\___\/////\\\_\/\\\_______\/\\\_\/\\\/////////_________\////\\\______    |
# |     ___\//\\\/\\\/\\\/\\\____\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\_____________________\////\\\___   |
# |      ____\//\\\\\\//\\\\\_____\/\\\_______\/\\\_\//\\\______/\\\__\/\\\______________/\\\______\//\\\__  |
# |       _____\//\\\__\//\\\______\//\\\\\\\\\\\\/___\///\\\\\\\\\/___\/\\\_____________\///\\\\\\\\\\\/___ |
# |        ______\///____\///________\////////////_______\/////////_____\///________________\///////////_____|
# '----------------------------------------------------------------------------------------------------------'
# By Alexander D. Steele ------------------------------- Student ID: 011226486 -------------- DATE: 10/24/2023
import threading
from datetime import datetime
from pathlib import Path

from src.datatypes.address import Address
from src.datatypes.truck import Truck
from src.services.package_loader import package_loader
from src.ui.load_animation import loading_animation
from src.ui.ui_methods import display_title, display_credit
from src.utils.csv_parser import read_csv

if __name__ == '__main__':

    # Start Title Screen display
    display_title()
    display_credit()

    # Start the threading for the loading animation while the main algorithm starts with the program
    stop = threading.Event()
    load = threading.Thread(target=loading_animation, args=(stop,))
    load.start()

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
    minimum_capacity = min([truck.max_inv for truck in trucks])

    # Day Start
    day_start = datetime.strptime("8:00 am", '%I:%M %p')
    hub = addresses[0]

    # Load packages at the start of the day
    packages = package_loader(addresses, packages_file, trucks, "8:00 am")
    packages_set = set()
    for key, package in packages:
        packages_set.add(package)

    # Stop the loading animation thread
    stop.set()
    load.join()
