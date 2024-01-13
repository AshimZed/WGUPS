class Address:
    def __init__(self, index, name, address):
        self.index = index
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}\t{self.address}"
