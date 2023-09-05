import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = list()
        for item in kwargs:
            value = kwargs.get(item)
            for _ in range(value):
                self.contents.append(item)


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#     pass
