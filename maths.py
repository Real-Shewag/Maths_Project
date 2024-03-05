print('1.Area of a triangle')
print('2.Area of a Rectangle')
print('3.Area of a Circle')
print('4.Area of a Square')
print('5.Area of a Rhombus')
pie="global variable"
pie=3.14
num=int(input('Enter your choice(hint:Enter the serial numbers of objects) : '))
def Area():
    def triangle():
        l=float(input("Enter the height : "))
        b=float(input("Enter the base : "))
        area=1/2*l*b
        print(f"Area of the triangle is {area}")
    def rectangle():
        l=float(input("Enter the height : "))
        b=int(input("Enter the breadth : "))
        
        area=2*(l+b)
        print(f"Area of the rectangle is {area}")
        
    def circle():
        r=float(input("Enter the radius : "))
        area=pie*r*r
        print(f"Area of the square is {area}")


    def square():
        a=float(input("Enter the side of square: "))
        area=4*a
        print(f"Area of square is {area}")
        
    def rhombus():
        d1=float(input("Enter first diaognal: "))
        d2=float(input("Enter second diaognal: "))
        area=d1*d2/2
        print(f"Area of the rhombus is {area}")
            
        
    if num==1:
        triangle()
    if num==2:
        rectangle()
    if num==3:
        circle()
    if num==4:
        square()
    if num==5:
        rhombus()
        
        
        
        











