import math

# Define fuction variables
a = int(input(" A: "))
b = int(input(" B: "))
c = int(input(" C: "))

class QuadraticEquation:
    # Initialize Variables
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    # Return the Discriminant
    def getDiscriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)
    # Find the first root
    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.getDiscriminant())) / (2 * self.a)
    # Find the second root
    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.getDiscriminant())) / (2 * self.a)

# Final Answer
k = QuadraticEquation(a,b,c)
print(k.getRoot1())
print(k.getRoot2())
print(k.getDiscriminant())
