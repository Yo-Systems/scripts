class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14
    def volume(self):
        return self.height*self.pi*(self.radius**2)
    
    def surface_area(self):
        return (2*self.pi*self.radius*self.height)+2*self.pi*self.radius**2