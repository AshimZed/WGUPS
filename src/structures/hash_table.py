import math

from src.structures.linked_list import LinkedList, Node


def next_power_of_2(x):
    return 1 if x == 0 else 2 ** (x - 1).bit_length()


def next_prime(current_prime):
    if current_prime == 2:
        return 3

    prime_found = False
    x = current_prime
    if x % 2 == 0:
        x += 1
    else:
        x += 2

    while not prime_found:
        is_prime = True
        for y in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            prime_found = True
        else:
            x += 2
    return x


# Adapted from the Mid-square Hash Function in the zyBooks (Lysecky et al.)
def mid_square_hash(key, n):
    # Determine the number of bits, R, based on N
    r = next_power_of_2(n).bit_length()

    # Scale key to handle poor distribution of low key values
    key *= 254927  # random prime with 6 digits

    # Square the key
    squared_key = key * key

    # Convert the squared key to binary
    squared_key_bin = bin(squared_key)[2:]  # slicing to remove 0b
    length = len(squared_key_bin)

    # Calculate the number of low bits to remove
    low_bits = (length - r) // 2

    # Extract the middle R bits
    extracted_bits = squared_key_bin[low_bits: low_bits + r]

    # Convert the binary string back to an integer
    extracted_bits = int(extracted_bits, 2)
    # Return hashed key
    return extracted_bits % n


# Iterator for the custom hash to make it easy to run the algorithm through it
class CustomHashTableIterator:
    def __init__(self, hash_table):
        self._hash_table = hash_table
        self._bucket_idx = 0
        self._bucket_iter = iter(self._hash_table.buckets[0])

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(self._bucket_iter)
            except StopIteration:
                # Move to the next bucket
                self._bucket_idx += 1
                if self._bucket_idx >= self._hash_table.num_buckets:
                    raise StopIteration
                self._bucket_iter = iter(self._hash_table.buckets[self._bucket_idx])


# Adapted from the Hash Tables and Functions in the zyBooks (Lysecky et al.)
class CustomHashTable:
    def __init__(self, num_buckets=8):
        self.num_buckets = num_buckets
        self.items = 0
        self.buckets = [LinkedList() for _ in range(self.num_buckets)]

    def __iter__(self):
        return CustomHashTableIterator(self)

    # Use the mid-square hash function to get the index
    def _hash(self, key):
        return mid_square_hash(key, self.num_buckets)

    # Amount of buckets is halved when the load factor suggests the table is too large
    def downsize(self):
        old_buckets = self.buckets
        self.num_buckets //= 2
        self.buckets = [LinkedList() for _ in range(self.num_buckets)]
        self.items = 0

        for bucket in old_buckets:
            if not bucket.is_empty:
                current_node = bucket.head
                while current_node is not None:
                    self.insert(current_node.key, current_node.data)
                    current_node = current_node.next

    # The table is resized to limit collisions when the load factor suggests the table is too small
    def upsize(self):

        old_buckets = self.buckets
        self.num_buckets = next_prime(self.num_buckets * 2)
        self.buckets = [LinkedList() for _ in range(self.num_buckets)]
        self.items = 0

        for bucket in old_buckets:
            if not bucket.is_empty:
                current_node = bucket.head
                while current_node is not None:
                    self.insert(current_node.key, current_node.data)
                    current_node = current_node.next

    # Insert a new key-value pair into the hash table
    def insert(self, key, item):
        if self.get(key) is None:
            bucket = self.buckets[self._hash(key)]
            node = Node(key, item)
            node.next = None
            bucket.insert(node)
            self.items += 1
        if self.load_factor() > 0.75:
            self.upsize()

    # Get a value from the hash table by its key
    def get(self, key):
        bucket = self.buckets[self._hash(key)]
        item = bucket.search(key)
        if item is not None:
            return item.data
        else:
            return None

    # Delete a key-value pair from the hash table
    def delete(self, key):
        bucket = self.buckets[self._hash(key)]
        node = bucket.search(key)
        if node is not None:
            bucket.remove(node)
            self.items -= 1
        if self.load_factor() < 0.25:
            self.downsize()

    def load_factor(self):
        return self.items / self.num_buckets
