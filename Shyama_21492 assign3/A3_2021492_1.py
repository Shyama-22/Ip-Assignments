import math
def matmul4(A,B):
    result = [0, 0, 0, 0]
    s = 0
    for a in range(len(A)):
        for b in range(len(B)):
            s = s + A[a][b] * B[b]
        result[a] += s
        s = 0
    return result
def matmul(A, B):
    result = []
    l = []
    if not str(B[0]).isnumeric:
        for i in range(len(A)):
            for j in range(len(B[0])):
                l.append(0)
            result.append(l)
            l = []
    else:
        result=[0,0,0]
    if not str(B[0]).isnumeric:
        for a in range(len(A)):
            for b in range(len(B[0])):
                for c in range(len(B)):
                    result[a][b] += A[a][c] * B[c][b]
    else:
        s = 0
        for a in range(len(A)):
            for b in range(len(B)):
                s=s+A[a][b] * B[b]
            result[a] +=s
            s=0
    return result
def scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    B = [x, y, z]
    A = [[sx, 0, 0], [0, sy, 0], [0, 0, sz]]
    fmat = matmul(A, B)
    l = [true_x, true_y, true_z]
    try:
        assert (l == fmat), 'False'
        return True
    except AssertionError:
        print('False')
        print('There is a problem!')
        return ""


def translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    B = [x, y, z, 1]
    A = [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz]]
    fmat = matmul(A, B)
    l = [true_x, true_y, true_z]
    try:
        assert (l == fmat), 'False'
        return True
    except AssertionError:
        print('False')
        print('There is a problem!')
        return ""

def rotation(x, y, z, axis, phi, true_x, true_y, true_z):
    angle = phi * math.pi / 180
    c = math.cos(angle)
    s = math.sin(angle)

    if axis == 'x':
        B = [x, y, z,1]
        A = [[1, 0, 0,0], [0, c, -s,0], [0, s, c,0],[0,0,0,1]]
        fmat = matmul4(A, B)
        transformedpoint = [fmat[0], fmat[1], fmat[2]]
        l = [true_x, true_y, true_z]
        try:
            assert (l == transformedpoint), 'False'
            return True
        except AssertionError:
            print('False')
            print('There is a problem!')
            return ""
    if axis == 'y':
        B = [x, y, z,1]
        A = [[c, 0, s,0], [0, 1, 0,0], [-s, 0, c,0],[0,0,0,1]]
        fmat = matmul4(A, B)
        transformedpoint = [fmat[0], fmat[1], fmat[2]]

        l = [true_x, true_y, true_z]

        try:
            assert (l == transformedpoint), 'False'
            return True
        except AssertionError:
            print('False')
            print('There is a problem!')
            return ""
    if axis == 'z':
        B = [x, y, z,1]
        A = [[c, -s, 0,0], [s, c, 0,0], [0, 0, 1,0],[0,0,0,1]]
        fmat = matmul4(A, B)
        transformedpoint = [fmat[0], fmat[1], fmat[2]]
        l = [true_x, true_y, true_z]
        try:
            assert (l == transformedpoint), 'False'
            return True
        except AssertionError:
            print('False')
            print('There is a problem!')
            return ""

print(rotation(1,0,0,'y',180,1,0,0))
# point = list(map(int, input('POINT').split()))
# tpt = list(map(int, input('TRUE POINT').split()))
# query = list(map(str, input("QUERY").split()))
# x = point[0]
# y = point[1]
# z = point[2]
# tx = tpt[0]
# ty = tpt[1]
# tz = tpt[2]
# if query[0] == "S":
#     print(scale(x, y, z, int(query[1]), int(query[2]), int(query[3]), tx, ty, tz))
# elif query[0] == "T":
#     print(translate(x, y, z, int(query[1]), int(query[2]), int(query[3]), tx, ty, tz))
# elif query[0] == "R":
#     print(rotation(x, y, z, int(query[1]), int(query[2]), tx, ty, tz))