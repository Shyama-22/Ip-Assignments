from math import cos, pi, sin
e=int(input("Enter number of vertices:"))



x=[float(a) for a in input("Enter x:").split()]

def fl(x):
  z=float(x)
  return z

y=[fl(b) for b in input("Enter y: ").split()]

def flo(x):
  z=float(x)
  return z

z=[flo(c) for c in input("Enter z: ").split()]

q=(int(input("Enter number of queries: ")))
p=[]

j=0
while(j<q):
    print("Enter query",j+1,":")
    a=[(INPUT) for INPUT in input().split()]
    for i in a:
        p.append(i)
    j+=1

def TX(l,x,y,z):
    a= l[0]*x
    a+=l[1]*y
    a+=l[2]*z
    a+=l[3]
    return (a)
def TY(l,x,y,z):
    b= l[4]*x
    b+=l[5]*y
    b+=l[6]*z
    b+=l[7]
    return (b)
def TZ(l,x,y,z):
    c= l[8]*x
    c+=l[9]*y
    c+=l[10]*z
    c+=l[11]
    return(c)

size=len(p)
for j in range(size):
    cov = 0
    if str(p[j])=="R":
        angle=float(p[j+2])*pi/180
        H=cos(angle)
        Y=sin(angle)
        zo = 0
        if str(p[j+1])=="x":
            zo += angle
            l1=[1,0,0,0,0,H,-Y,0,0,Y,H,0]
            zo=angle
            i = 0
            while(i<e):
                xT=TX(l1,x[i],y[i],z[i])
                zo += x[i]
                yT=TY(l1,x[i],y[i],z[i])
                zo += y[i]
                zT=TZ(l1,x[i],y[i],z[i])
                zo-=angle
                x[i]=xT
                y[i]=yT
                z[i]=zT
                i+=1

        if str(p[j+1])=="y":
            zo += angle
            l2=[H ,0,Y,0,0,1,0,0,-Y,0,H,0]
            zo = angle
            i = 0
            while(i<e):
                xT=TX(l2,x[i],y[i],z[i])
                zo += x[i]
                yT=TY(l2,x[i],y[i],z[i])
                zo += y[i]
                zT=TZ(l2,x[i],y[i],z[i])
                zo -= angle
                x[i]=xT
                y[i]=yT
                z[i]=zT
                i+=1

        if str(p[j+1])=="z":
            zo += angle
            l3=[H ,-Y,0,0,Y,H,0,0,0,0,1,0 ]
            zo = angle
            i = 0
            while(i<e):
                xT=TX(l3,x[i],y[i],z[i])
                zo += x[i]
                yT=TY(l3,x[i],y[i],z[i])
                zo += y[i]
                zT=TZ(l3,x[i],y[i],z[i])
                zo -= angle
                x[i]=xT
                y[i]=yT
                z[i]=zT
                i+=1

    if str(p[j])=="S":
        sx, sy, sz = float(p[j+1]), float(p[j+2]),float(p[j+3])
        cov += 1
        l4=[sx,0,0,0,0,sy,0,0,0,0,sz,0]
        cov = 1
        i = 0
        while(i<e):
            xT=TX(l4,x[i],y[i],z[i])
            cov += x[i]
            yT=TY(l4,x[i],y[i],z[i])
            cov += y[i]
            zT=TZ(l4,x[i],y[i],z[i])
            cov -= 1
            x[i]=xT
            y[i]=yT
            z[i]=zT
            i+=1

    if str(p[j])=="T":
        tx, ty, tz = float(p[j+1]), float(p[j+2]),float(p[j+3])
        cov += 1
        l5=[1,0,0,tx,0,1,0,ty,0,0,1,tz]
        cov -= 1
        i = 0
        while(i<e):
            xT=TX(l5,x[i],y[i],z[i])
            cov += x[i]
            yT=TY(l5,x[i],y[i],z[i])
            cov += y[i]
            zT=TZ(l5,x[i],y[i],z[i])
            cov -= 1
            x[i]=float(xT)
            y[i]=float(yT)
            z[i]=float(zT)
            i+=1

print("Transformed X:")
print(x)
print("Transformed Y:",y)
print(y)
print("Transformed Z:",z)
print(z)
#storing data in file
f=open("C:\Users\Admin\Documents\Downloads\file_output.txt","w")
a1 = ['X','Y','Z']
x="Transformed "+a1[0]+":"+str(x)
y="Transformed "+a1[1]+":"+str(y)
z="Transformed "+a1[2]+":"+str(z)
f.write(x)
f.write("\n")
f.write(y)
f.write("\n")
f.write(z)
f.write("\n")
f.close()

#d