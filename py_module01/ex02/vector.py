class Vector:
    def __init__(self, values):
        if type(values) == list and len(values) and type(values[0]) == list:
            self.values = values
        elif type(values) == int and values > 0:
            self.values = [[i] for i in range(values)]
        elif type(values) == tuple and len(values) == 2 and type(values[0]) == int and type(values[1]) == int and values[0] <= values[1]:
            self.values = [[i] for i in range(values[0], values[1])]
        else:
            raise IndentationError("not defined")
        self.shape = (0 if (len(self.values) == 0) else len(values), len(values[0]))
    def __add__(self, x):
        if self.calculateShape(x) != self.shape:
            raise ValueError("not the sape shape")

        
