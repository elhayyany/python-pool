class Vector:
    def calculate_shape(values):
        if not isinstance(values, list) or not all(len(values) != 1 and len(values[x]) != 1 for x in values):
            raise ValueError("bad atgument")
        if len(values) == 1:
            return (1, len(values[0]))    
        return (len(values), 1)

    def __init__(self, values):
        self.values = values
        self.shape = calculate_shape(values)
    def __add__(self, x):
        pass
        
