import os
import csv


def initialize_log_file(file_path, headers):
    # Check if the file exists
    file_exists = os.path.exists(file_path)

    # Open the file in write mode ('w') to create or clear it
    with open(file_path, 'w', newline='') as file:
        # If the file didn't exist or needs headers, write them
        if not file_exists or headers:
            writer = csv.writer(file)
            writer.writerow(headers)
