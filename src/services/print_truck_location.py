import csv
from datetime import datetime

from src.datatypes.status import Status


def print_truck_location(log_file, trucks, packages, check_time, truck_id):
    truck = next((truck for truck in trucks if str(truck.truck_id) == truck_id), None)
    if not truck:
        print(f"No package found with ID: {truck_id}")
        return

    log_entries = []
    with open(log_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if str(truck_id) == row[3]:
                time = datetime.strptime(row[0], '%I:%M %p')
                package_id = row[1]
                status = row[2]
                log_entries.append([time, package_id, status, truck_id])

    log_entries.sort(key=lambda x: x[0])
    check_time = datetime.strptime(check_time, '%I:%M %p')

    next_known_status = None

    for i in range(len(log_entries)):
        if log_entries[i][0] <= check_time:
            if i == len(log_entries) - 1 or log_entries[i + 1][0] > check_time:
                if i + 1 < len(log_entries):
                    next_known_status = log_entries[i + 1][2]
                    package = next((pkg for pkg in packages if str(pkg.package_id) == log_entries[i + 1][1]), None)
                break

    if next_known_status is None:
        print(f"Truck {truck_id} done for day")
    elif next_known_status == str(Status.EN_ROUTE):
        print(f"Truck {truck_id} is heading to the depot.")
    elif next_known_status == str(Status.DELIVERED):
        print(f"Truck {truck_id} is delivering Package ID: {package.package_id} to {package.address}")