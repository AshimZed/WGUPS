from enum import Enum


class Status(Enum):
    AT_DEPOT = 'AT_DEPOT'  # For packages at the hub waiting to be routed
    DELAYED_ON_FLIGHT = 'DELAYED_ON_FLIGHT'  # For packages that are delayed
    DELIVERED = 'DELIVERED'  # For packages arrived at locations
    EN_ROUTE = 'EN_ROUTE'  # For packages in trucks
    REROUTING = 'REROUTING'  # For packages with issues such as 'Wrong Address'

    def __str__(self):
        return self.value
