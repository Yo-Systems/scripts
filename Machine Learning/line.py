class Line:

    def init(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

     def distance(self):
        return ((self.coor2[0]-self.coor1[0])2 + (self.coor2[1]-self.coor1[1])2)**0.5

    def slope(self):
        if self.coor1[0] == self.coor2[0]:
            return "undefined"

        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])