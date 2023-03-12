import copy
import random
from random import choice
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for colour, value in kwargs.items():
            for n in range(value):
                self.contents.append(colour)

    def draw(self, number):
        removed_balls = []
        if number > len(self.contents):
            return self.contents

        for n in range(number):
            ball = choice(self.contents)
            removed_balls.append(ball)
            self.contents.remove(ball)

        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    exp_balls = []

    for colour, value in expected_balls.items():
        for n in range(value):
            exp_balls.append(colour)
    count = 0
    new_hat = copy.deepcopy(hat.contents)

    for colour in range(num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(new_hat)
        new_count = 0
        for colour in exp_balls:
            for value in balls_drawn:
                if colour == value:
                    new_count += 1
                    balls_drawn.remove(value)
                    break
        if new_count == len(exp_balls):
            count += 1

    return count/num_experiments
