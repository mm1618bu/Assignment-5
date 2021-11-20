class LinearEquation:
#class variables
    
#constructor
    def __init__(self,a, b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


#getter setter methods
    def getA(self):
        self.a = int(input(" "))
        return self.a
    def getB(self):
        self.b = int(input(" "))
        return self.b
    def getC(self):
        self.c = int(input(" "))
        return self.c
    def getD(self):
        self.d = int(input(" "))
        return self.d
    def getE(self):
        self.e = int(input(" "))
        return self.e
    def getF(self):
        self.f = int(input(" "))
        return self.f

#check method is solvable
    def isSolvable(self):
        if((self.a*self.d - self.b*self.c) == 0):
            print('The equation has no solution')
        else:
            print('The equation has solution')
# methods to calculate X and Y
    def getX(self):
        return (self.e*self.d - self.b*self.f) / (self.a*self.d - self.b*self.c)

    def getY(self):
        return (self.a*self.f - self.e*self.c) / (self.a*self.d - self.b*self.c)


Linear = LinearEquation(2,22,222,2222,22222,222222)
#calling methods
Linear.isSolvable()
print('X value: ',Linear.getX())
print('Y value: ',Linear.getY())
