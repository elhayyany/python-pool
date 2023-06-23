class Vector:
    def __init__(self, values):
        self.values = values
        if not isinstance(values, list) or not all(len(values) != 1 and len(values[x]) != 1 for x in values):
            raise ValueError("bad atgument")
        if len(values) == 1:
            self.shape = (1, len(values[0]))
        else:
            self.shape = (len(values), 1)
        print(self.shape)