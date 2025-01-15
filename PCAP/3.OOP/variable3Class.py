class ExampleClass:
    def __init__(self, val):
        self.a=0
        self.b=0
        if val % 2 != 0:
            self.a = val
        else:
            self.b = 1


example_object = ExampleClass(11)

print(example_object.a)
print(example_object.b)