# Formula
# number of cans = ( wall height x wall width) / coverage per can
import math

coverage = 5
test_h = float(input("Type your height:"))
test_w = float(input("Type your width:"))


def paint_calc(h, w):
    cans = float((h * w)/ coverage)
    round_up = math.ceil(cans)
    print(f"you'll need {round_up} cans to paint this area")
    

paint_calc(test_h,test_w)