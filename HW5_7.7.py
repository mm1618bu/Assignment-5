# Set the inital variables
a = int(input("Value of A"))
b = int(input("Value of B"))
c = int(input("Value of C"))
d = int(input("Value of D"))
e = int(input("Value of E "))
f = int(input("Value of F "))

class LinearEquation:
# Activate Variables
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


#Setter Method Initialize
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getD(self):
        return self.d
    def getE(self):
        return self.e
    def getF(self):
        return self.f

#Solvable Method
    def isSolvable(self):
        if((self.a*self.d - self.b*self.c) == 0):
            print('The equation has no solution')
        else:
            print('The equation has solution')
# Find X and Y
    def getX(self):
        return (self.e*self.d - self.b*self.f) / (self.a*self.d - self.b*self.c)

    def getY(self):
        return (self.a*self.f - self.e*self.c) / (self.a*self.d - self.b*self.c)


Linear = LinearEquation(a,b,c,d,e,f)
#calling methods
Linear.isSolvable()
print('X value: ',Linear.getX())
print('Y value: ',Linear.getY())
