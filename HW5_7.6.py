import math

a = int(input(" A: "))
b = int(input(" B: "))
c = int(input(" C: "))

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.getDiscriminant())) / (2 * self.a)
    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.getDiscriminant())) / (2 * self.a)

k = QuadraticEquation(a,b,c)
print(k.getRoot1())
print(k.getRoot2())
print(k.getDiscriminant())
