import copy
import random


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = list()
        for item in kwargs:
            value = kwargs.get(item)
            for _ in range(value):
                self.contents.append(item)

    def draw(self, balls_to_draw):
        if balls_to_draw < len(self.contents):
            balls_drawn = list()
            for _ in range(balls_to_draw):
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                balls_drawn.append(random_ball)
            return balls_drawn
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        new_hat = copy.deepcopy(hat)

        balls_drawn = new_hat.draw(num_balls_drawn)
        found_all = True
        for key in expected_balls:
            if balls_drawn.count(key) < expected_balls[key]:
                found_all = False
                break

        if found_all:
            success_count += 1

    probability = success_count / num_experiments
    return probability
