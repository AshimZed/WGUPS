import csv
from datetime import datetime


def print_package(log_file, packages, check_time, package_id):
    package = next((pkg for pkg in packages if str(pkg.package_id) == package_id), None)
    if not package:
        print(f"No package found with ID: {package_id}")
        return

    log_entries = []
    with open(log_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if str(package_id) == row[1]:
                time = datetime.strptime(row[0], '%I:%M %p')
                status = row[2]
                truck = row[3]
                log_entries.append([time, package_id, status, truck])

    log_entries.sort(key=lambda x: x[0])
    check_time = datetime.strptime(check_time, '%I:%M %p')

    last_known_status = None

    for i in range(len(log_entries)):
        if log_entries[i][0] <= check_time:
            if i == len(log_entries) - 1 or log_entries[i + 1][0] > check_time:
                last_known_status = log_entries[i][2]
                truck = log_entries[i][3]
                break

    # Print the last known status if found
    if last_known_status:
        print(f"{datetime.strftime(check_time, '%I:%M %p')} | {last_known_status} | Truck: {truck} | {package}")
    else:
        print("No status found for the specified time and package ID.")
