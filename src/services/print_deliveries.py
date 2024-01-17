import csv
from datetime import datetime

from src.datatypes.status import Status


def print_deliveries(log_file, trucks, check_time, truck_id):
    truck = next((truck for truck in trucks if str(truck.truck_id) == truck_id), None)
    if not truck:
        print(f"No truck found with ID: {truck_id}")
        return

    log_entries = []
    with open(log_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if str(truck_id) == row[3] and str(Status.DELIVERED) == row[2]:
                time = datetime.strptime(row[0], '%I:%M %p')
                package_id = row[1]
                status = row[2]
                log_entries.append([time, package_id, status, truck_id])

    log_entries.sort(key=lambda x: x[0])
    check_time = datetime.strptime(check_time, '%I:%M %p')

    for idx, entry in enumerate(log_entries):
        if entry[0] > check_time:
            log_entries = log_entries[:idx]
            break

    for entry in log_entries:
        print(f"Time: {datetime.strftime(entry[0], '%I:%M %p')} | Package ID: {entry[1]}"
              f" | Status: {entry[2]} | Truck: {entry[3]}")
