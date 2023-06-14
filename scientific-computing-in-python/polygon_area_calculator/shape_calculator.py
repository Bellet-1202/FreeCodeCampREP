class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2 * (self.height + self.width)
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
    
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      string_result = "Too big for picture."
      return string_result
    else:
      string_result=""
      for i in range(0,self.height):
        string_result += "*"
        for j in range(0,self.width-1):
          string_result += '*'
        string_result += "\n"
    return string_result
        
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        
  def get_amount_inside(self,Rectangle):
    return (self.width*self.height) // (Rectangle.width * Rectangle.height)


class Square(Rectangle):
  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side
    
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
