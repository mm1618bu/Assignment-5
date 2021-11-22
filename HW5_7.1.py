#! /usr/bin/python3

# Define Rectangle Class
class Rectangle:
	# Initialize Width and Height
	def __init__(self,width,height):
		self.width = width
		self.height = height
	# Return the area
	def getArea(self):
		return self.width * self.height
	# Return the Permimiter
	def getPerimeter(self):
		return(self.height + self.height) * 2

# Run the Program with the desired parameters

def main():
    width1, height1 = 4,40
    width2, height2 = 3.5,35.7
    rect1 = Rectangle(width1, height1)
    rect2 = Rectangle(width2, height2)

    print("Calculations for rectangle one: ")
    print(" Width: ",width1,'\n'," Height: ",height1,'\n'," Area: ",rect1.getArea(),'\n'," Perimeter: ", rect1.getPerimeter())
    print("Calculations for rectangle two: ")
    print(" Width: ",width2,'\n'," Height: ",height2,'\n'," Area: ",rect2.getArea(),'\n', " Perimeter: ", rect2.getPerimeter())

main()
