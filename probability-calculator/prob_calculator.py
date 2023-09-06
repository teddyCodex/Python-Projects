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
    success_count = int()
    for i in range(num_experiments):
        new_hat = copy.copy(hat)
        list_of_balls = new_hat.draw(num_balls_drawn)
        print(list_of_balls)
        check = []
        for ball in expected_balls:
            print(ball)
            ball_count = list_of_balls.count(ball)
            if ball_count >= expected_balls.get(ball):
                check.append(True)
        print(check)
        if len(check) >= len(expected_balls):
            success_count += 1

    # print(success_count)

    return success_count / num_experiments


hat = Hat(blue=3, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=1,
)
print(probability)

expected = 0.272

# hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
# probability = experiment(
#     hat=hat,
#     expected_balls={"yellow": 2, "blue": 3, "test": 1},
#     num_balls_drawn=20,
#     num_experiments=100,
# )
# print(probability)
# expected = 1.0
