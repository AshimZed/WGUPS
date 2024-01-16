import csv


def log_package_event(log_file, time, package, status, truck=None):
    str_time = time.strftime('%I:%M %p')
    event = str(status)
    if truck is not None:
        truck_id = str(truck.truck_id)
    else:
        truck_id = "Not Assigned"
    with open(log_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str_time, package.package_id, event, truck_id])
