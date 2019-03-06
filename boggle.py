def make_grid(width, height):
  """
  create grid that will hold all the squares - empty dictionary for row and height
  """
  return{(row,col): '' for row in range(height)
      for col in range(width)}