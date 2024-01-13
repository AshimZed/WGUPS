
def miles_to_hours(miles, speed):
    return miles / speed


def get_distance(distance_matrix, address_a, address_b):
    if distance_matrix[address_a.index][address_b.index] is None:
        # If function checks the wrong side of the diagonal, swap the indices
        return distance_matrix[address_b.index][address_a.index]
    else:
        return distance_matrix[address_a.index][address_b.index]
    