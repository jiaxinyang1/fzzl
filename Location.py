from enum import Enum,unique


class pos():
    def __init__(self,x,y):
        self.x=x
        self.y=y

@unique
class Location(Enum):
    four_four= pos(1041,409)
    three_four =pos(1043,229)
    four_three=pos(712,269)
    three_three=pos(737,431)
    Sakura_three_ten=pos(1110,431)
    Sakura_three_one=pos(116,255)

