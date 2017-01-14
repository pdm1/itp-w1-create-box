"""This is the entry point of the program."""


def create_box(height, width, character):
  a_str = ""
  if height is 0 or width is 0:
    return "Either height or width is incorrect"
  for row in range(height):
    for col in range(width):
      a_str += character
    a_str += "\n"
  print(a_str)
  return a_str
  
def create_outer_box(height,width,char="!"):
  a_str = ""
  if height is 0 or width is 0:
    return "Either height or width is incorrect"
  if width is 1 and height > 1:
      a_str = (char + "\n")*height
      print(a_str)
      return a_str
  else:
    for row in range(height):
      for col in range(1):
        if row is 0 or row is height - 1:
          a_str += char*width + "\n"
        elif col > 0 or col < width - 1:
          a_str += str(char + " " * (width - 2) + char + "\n") 
    print(a_str)
    return a_str
  


if __name__ == '__main__':
    create_box(3, 4, '*')
    create_outer_box(6,9)
