import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self,**kwargs):
    hat_dict = kwargs
    self.contents = []

    for color in hat_dict:
      num_times = hat_dict[color]
      for i in range(num_times):
        self.contents.append(color)

  def draw(self, num_balls_drawn):
    cur_contents = self.contents
    drawn_balls = []

    if num_balls_drawn >= len(cur_contents):
      return cur_contents
    else:
      for i in range(num_balls_drawn):
        ball = random.randrange(len(cur_contents))
        drawn_balls.append(cur_contents.pop(ball))
      return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_match = 0

  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)

    drawn_balls = hat_copy.draw(num_balls_drawn)
    actual_balls = {}

    for ball in drawn_balls:
      actual_balls[ball] = actual_balls.get(ball,0) + 1

    matching_balls = {}

    for key in expected_balls:
      if (key in actual_balls and expected_balls[key] <= actual_balls[key]):
        matching_balls[key] = expected_balls[key]
      else:
        break
    
    if matching_balls == expected_balls:
      num_match += 1

  probability = num_match / num_experiments

  return probability
