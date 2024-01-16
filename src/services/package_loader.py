from datetime import datetime

from src.datatypes.package import Package
from src.datatypes.status import Status
from src.structures.hash_table import CustomHashTable
from src.utils.csv_parser import read_csv
from src.utils.log_event import log_package_event


def match_address(address_list, address_string):
    for address in address_list:
        if address.address == address_string:
            return address
    return None


def handle_comment(package, active_truck_ids):
    # Grab comment and lower all case
    comment = package.comment.lower()

    # Handle packages that need to be delivered together
    if "must be delivered with" in comment:
        # Grab the IDs from the comment and store them in the packages linked_packages
        linked_ids = [int(package_id.strip()) for package_id in comment.split("with")[1].split(",")]
        for lpkg_id in linked_ids:
            package.linked_packages.add(lpkg_id)

    # Handle wrong addresses
    if "wrong address" in comment:
        package.status = Status.REROUTING
        datetime_conversion = datetime.strptime("10:20 AM", '%I:%M %p')
        package.available_time = datetime_conversion

    # Handle truck assignment limitations
    if "can only be on truck" in comment:
        allowed_truck = int(comment.split()[-1])
        banned = [truck.truck_id for truck in active_truck_ids if truck.truck_id != allowed_truck]
        package.banned_trucks = banned

    # Handle packages delayed on flight
    if "delayed on flight" in comment:
        package.status = Status.DELAYED_ON_FLIGHT
        eta = " ".join(comment.split()[-2:])
        datetime_conversion = datetime.strptime(eta, '%I:%M %p')
        package.available_time = datetime_conversion


def package_loader(address_list, packages_file, active_truck_ids, current_time, log_file):
    # Instantiate database
    packages = CustomHashTable()

    # Parse packages csv file and store in custom hash table
    data = read_csv(packages_file)
    for row in data:
        package_id = int(row[0])
        # Find the address that matches the street address in the data
        address = match_address(address_list, row[1])
        city = row[2]
        state = row[3]
        zipcode = row[4]
        # Convert deadline string into a datetime object and set EOD deadlines to 5:00 pm
        deadline = (datetime.strptime(row[5], "%I:%M %p")
                    if row[5] != "EOD" else None)
        # Weight kept as a string because converting into a float is unnecessary and outside the scope of the assignment
        weight = row[6]
        comment = row[7] if row[7] else ''
        package = Package(package_id, address, city, state, zipcode, deadline, weight, comment, current_time)
        handle_comment(package, active_truck_ids)
        log_package_event(log_file, (datetime.strptime(current_time, '%I:%M %p')), package, package.status)
        packages.insert(package_id, package)

    return packages
