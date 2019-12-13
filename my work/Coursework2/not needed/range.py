
def vertical_lost_range(x,y):
    lost_range = [[x,y]]
    while y < 700:
        y += 25
        lost_range.append([x,y])
    return lost_range


def horizontal_lost_range(x,y):
    lost_range = [[x,y]]
    while x < 700:
        x += 25
        lost_range.append([x,y])
    return lost_range



lost1 = [(horizontal_lost_range(0.0,700.0)), (vertical_lost_range(0.0,0.0))]
i = [0.0, 0.0]
print (lost1)
# if  i in lost1[0] or i in lost1[1]:
#     print (i)
# else:
#     print ("!")
