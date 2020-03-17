"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Initial serial number"
        self.start = start
        self.initial = start

    def generate(self):
        "Generates new serial number (+1 of original start_number)"
        self.start += 1
        return self.start - 1

    def reset(self):
        self.start = self.initial
