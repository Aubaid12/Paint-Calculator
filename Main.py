import math
def paint_calc(height,width,cover):
  area = height * width
  num_cans = math.ceil(area / cover)
  print(f"you need {num_cans} cans")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
