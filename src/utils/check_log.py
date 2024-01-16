import csv


def log_exists(log_file, package, status):
    with open(log_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if str(package.package_id) == row[1] and str(status) == row[2]:
                return True
    return False
