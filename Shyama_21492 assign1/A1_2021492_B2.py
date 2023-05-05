from enum import auto
import math
def ray_sphere_intersection(e,d,x0,y0,z0,r):
    a = d[0]**2 + d[1]**2 + d[2]**2
    b = 2*d[0]*(e[0] - x0) + 2*d[1]*(e[1] - y0) + 2*d[2]*(e[2] - z0)
    c = x0**2 + y0**2 + z0**2 + e[0]**2 + e[1]**2 + e[2]**2 - 2*(e[0]*x0 + e[1]*y0 + e[2]*z0) - r**2
    discriminant = b*b - 4*a*c
    if(discriminant < 0.0):  # no intersection 
        print("The ray of light does not intersects the sphere!")
    elif(discriminant == 0.0): # ray of light is tangent to sphere i.e they intersects at 1 point
        print("Ray of light is tangent to sphere i.e they intersects at 1 point")
        t = (-b - math.sqrt(discriminant)) / 2.0*a
        x = e[0] + t*d[0]
        y = e[1] + t*d[1]
        z = e[2] + t*d[2]
        print("intersection point is: {x} , {y} , {z}",x,y,z)
    elif(discriminant > 0.0):  # ray of light intersects sphere at 2 points
        print("Ray of light intersects sphere at 2 points")
        t0 = (-b - math.sqrt(discriminant)) / 2.0*a
        x1 = e[0] + t0*d[0]
        y1 = e[1] + t0*d[1]
        z1 = e[2] + t0*d[2]
        print("1st intersection point: {0} , {1} , {2}".format(x1,y1,z1))
        t = (-b + math.sqrt(discriminant)) / 2.0*a
        x = e[0] + t*d[0]
        y = e[1] + t*d[1]
        z = e[2] + t*d[2]
        print("2nd intersection point: {0} , {1} , {2}".format(x,y,z))
 
def main():
    e = []
    d = []
    print("Enter the origin of light ray 'e': ")
    for i in range(0,3):
        temp = float(input(f"x{i+1}--->"))
        e.append(temp)
    print("Enter the direction of light ray 'd': ")
    for i in range(0,3):
        temp = float(input(f"x{i+1}--->"))
        d.append(temp)
    x0 = float(input("Enter the x coordinate of origin of the sphere 'x0': "))
    y0 = float(input("Enter the y coordinate of origin of the sphere 'y0': "))
    z0 = float(input("Enter the z coordinate of origin of the sphere 'z0': "))
    r = float(input("Enter the radius of  the sphere 'R': "))
 
    ray_sphere_intersection(e,d,x0,y0,z0,r)
if __name__ == '__main__':
    main()