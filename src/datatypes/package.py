# Class to handle package objects
from datetime import datetime

from src.datatypes.status import Status


class Package:

    # Constructor
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, comment, available_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.comment = comment
        self.available_time = datetime.strptime(available_time, '%I:%M %p')

        # Fields to handle special circumstances
        self.banned_trucks = []
        self.status = Status.AT_DEPOT
        self.linked_packages = set()
        self.delivery_time = None
        self.has_constraint = False
        self.history = {}

    # String definition
    def __str__(self):
        return (f"Package ID: {self.package_id} | Weight: {self.weight} | Deadline: {self.deadline}"
                f" | Addressed: {self.address}")
