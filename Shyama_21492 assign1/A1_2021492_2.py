def twoD():
        print("[1] square\n[2] rectangle\n[3] rhombus\n[4] parallelogram\n[5] circle \n")
        print("Input your shape code like 1 for square and 2 for rectangle or enter 0 to exit : ")
        b = int(input())
        if b == 0:
            exit()
        if b == 1:
            print("Type in the side of the square")
            c = int(input())
            print("Perimeter of the square is ", 4*c)
            print("Area of the square is", c*c)

        elif b == 2:
            print("Enter the value of length")
            c = int(input())
            print("Enter the value of breadth")
            e = int(input())
            print("The perimeter of the rectangle is ", 2*(c+e))
            print("The area of the rectangle is", c*e)

        elif b == 3:
            print("Enter the value of side")
            c = int(input())
            print("Enter the value of Diagonal 1")
            e = int(input())
            print("Enter the value of Diagonal 2")
            f = int(input())
            print("The perimeter of the rhombus is ", 4*c)
            print("The area of the rhombus is", (f*e)/2)

        elif b == 4:
            print("Enter the value of length")
            c = int(input())
            print("Enter the value of breadth")
            e = int(input())
            print("Enter the value of height")
            f = int(input())
            print("The perimeter of the parallelogram is ", 2*(c+e))
            print("The area of the parallelogram is", (f*e))

        elif b == 5:
            print("Type in the radius")
            c = int(input())
            print("Circumference of the circle is ", 2*3.14*c)
            print("Area of the circle is", 3.14*c*c)

        else:
            print("No such shape detected")



def threeD():
        print("[1] cube\n[2] cuboid\n[3] right circular cone\n[4] hemisphere\n[5] sphere \n[6] solid cylinder\n[7] hollow cylinder\n")
        print("Input your shape code like 1 for cube and 2 for cuboid or enter 0 to exit : ")
        b = int(input())
        if b == 0:
            exit()
        if b == 1:
            print("Type in the side")
            c = int(input())
            print("CSA of the cube is ", 4*c*c)
            print("TSA of the cube is", 6 * c * c)
            print("Volume of the cube is", c * c * c)

        elif b == 2:
            print("Enter the value of length")
            c = int(input())
            print("Enter the value of breadth")
            e = int(input())
            print("Enter the value of height")
            f = int(input())
            print("The CSA of the cuboid is ", 2 * f*(c + e))
            print("The TSA of the cuboid is", (2*(c * e + e * f + c * f)))
            print("The volume of the cuboid is", c*f*e)

        elif b == 3:
            print("Enter the value of radius")
            c = int(input())
            print("Enter the value of Slant height")
            e = int(input())
            print("Enter the value of height")
            f = int(input())
            print("The CSA of the right circular cone is ", 3.14 * c*e)
            print("The TSA of the right circular cone is", (3.14*c*e*(c+e)))
            print("The volume of the right circular cone is", (3.14*c*f*c)/3)

        elif b == 4:
            print("Type in the radius")
            c = int(input())
            print("CSA of the hemisphere is ", 2*3.14*c*c)
            print("TSA of the hemisphere is", 3* 3.14*  c * c)
            print("Volume of the hemisphere is", 2/3*3.14*c * c * c)

        elif b == 5:
            print("Type in the radius")
            c = int(input())
            print("CSA of the sphere is ", 4*3.14*c*c)
            print("TSA of the sphere is", 4*3.14 * c * c)
            print("Volume of the sphere is", 4/3*3.14*c * c * c)

        elif b == 6:
            print("Enter the value of radius")
            c = int(input())
            print("Enter the value of height")
            f = int(input())
            print("The CSA of the solid cylinder is ", 2*3.14 * c*f)
            print("The TSA of the solid cylinder is", (2*3.14*c*(c+f)))
            print("The volume of the solid cylinder is", (3.14*c*f*c))


        elif b == 7:
            print("Enter the value of larger radius 1")
            c = int(input())
            print("Enter the value of radius 2")
            e = int(input())
            print("Enter the value of height")
            f = int(input())
            print("The CSA of the hollow cylinder is ", 2*3.14 * f * (c+e))
            print("The TSA of the hollow cylinder is", (2*3.14 * f * (c+e))+(2*3.14*(c*2-e*2)) )
            print("The volume of the hollow cylinder is", (3.14 * (c*2-e*2)*f))

        else:
            print("No such shape exists\n")



while True:
    print("The total number of students in the class are: ")
    n = int(input())

    for i in range(n):
        print("Type 1 for 2D shapes and 2 for 3D shapes or 3 to exit : ")
        a = int(input())
        if a == 1:
            twoD()


        if a == 2:
            threeD()
    
        if a == 3:
            exit()
    print("Do you want to enter for more students? type yes/no: ")
    ans=input()
    if(ans=="no"):
        print("Exiting The Program")
        break