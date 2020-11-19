class Rectangle:
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def __str__(self):
      return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
      self.width = width

  def set_height(self, height):
      self.height = height

  def get_area(self):
      area = self.height * self.width
      return area

  def get_perimeter(self):
      perimeter = (2 * self.width) + (2 * self.height)
      return perimeter

  def get_diagonal(self):
      diagonal = (self.height**2 + self.width**2)**.5
      return diagonal

  def get_picture(self):
      if self.width > 50 or self.height > 50:
          return "Too big for picture."
      else:
          picture = []
          for i in range(self.height):
              picture.append('*' * self.width + '\n')

          nl = ''
          return nl.join(picture)

  def get_amount_inside(self, shape):
      if self.height < shape.height or self.width < shape.width:
        return 0
      else:
        num_wide = int(self.width / shape.width)
        num_high = int(self.height / shape.height)

        return num_wide * num_high



class Square(Rectangle):
  def __init__(self, side):
      super().__init__(width=side, height=side)
      self.side = side

  def __str__(self):
      return f'Square(side={self.side})'

  def set_side(self, side):
      self.side = side
      self.width = side
      self.height = side

  def set_width(self, side):
      self.set_side(side)

  def set_height(self, side):
      self.set_side(side)
