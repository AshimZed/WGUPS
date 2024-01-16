from src.structures.hash_table import CustomHashTable
from src.utils.distance_functions import get_distance


class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.max_inv = 16
        self.speed_mph = 18
        self.inv = []
        self.route = None
        self.steps = None
        self.total_mileage = 0
        self.current_mileage = 0
