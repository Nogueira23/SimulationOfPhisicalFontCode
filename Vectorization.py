class Vectorization():
    def __init__(self):
        self.origin = [0,0]
        self.i = [1,0]
        self.j = [0,1]
    
    def vector(self, xp, yp):
        return [xp, yp]
    
    def diference(self, p1, p2):
        d = [p1[0]-p2[0], p1[1] - p2[1]]
        return d

    def sum(self, p1, p2):
        s = [p1[0]+p2[0], p1[1] + p2[1]]
        return s

    def module(self, p):
        module_p = (p[0]**2 + p[1]**2)**(1/2)
        return module_p
    
    def in_product(self, p1, p2):
        p = p1[0]*p2[0] +  p2[1]*p1[1]
        return p
    
    def projectation(self, origin, cord: str):
        if cord == 'x':
            origin_base_x = self.in_product(self.i, origin)*self.i[0]
            origin_base_y = self.in_product(self.i, origin)*self.i[1]
            return [origin_base_x, origin_base_y]
        if cord == 'y':
            origin_base_x = self.in_product(self.j, origin)*self.j[0]
            origin_base_y = self.in_product(self.j, origin)*self.j[1]
            return [origin_base_x, origin_base_y]