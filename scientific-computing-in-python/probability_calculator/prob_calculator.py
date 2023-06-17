import copy
import random

class Hat:
  
  def __init__(self, **kwargs):
    self.contents = [k for k, v in kwargs.items() for _ in range(v)]
        
  def get_colors(self):
    return list(self.colors)
    
  def get_contents(self):
    return self.contents
    
  def draw(self,number):
    if number >= len(self.contents):
      return self.contents
    else:
      list_of_draw = []
      for _ in range(0, number):
        random_number = random.randint(0,len(self.contents)-1)
        element_gone = self.contents.pop(random_number)
        list_of_draw.append(element_gone)
      return list_of_draw
        
def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    nums_positive = 0
    for _ in range(num_experiments):
        balls_got_drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        colors = [True if balls_got_drawn.count(key) >= value else False for key, value in expected_balls.items()]
        nums_positive += 1 if all(colors) else 0
    return nums_positive / num_experiments