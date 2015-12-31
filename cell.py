class Cell:
    def __init__(self, position, value):
        self.position = position
        self.value = value
        self.description = [position, value]

    def __str__(self):
        return str(self.value) 
