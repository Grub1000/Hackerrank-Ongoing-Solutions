import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)
    def cross(self, no):
        return Points((self.y * no.z - no.y * self.z), ((self.x * no.z - no.x * self.z)), (self.x * no.y - no.x * self.y))
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
    print(x.x, x.y,x.z)

# Notes: Dot Product
# If we have 2 vectors a = <a1, a2, a3> and b = <b1, b2, b3> Then the dot product will be -->
# --> a . b = (a1 * b1) + (a2 * b2) + (a3 * b3)
# The dot product results in a Scalar value. Not another vector!
# 
# The dot product also comes into play in the theorem that stats -->
# --> a . b = |a|*|b| * cos(Angle between both vectors) --> 
# --> therefore if we want the angle between both vectors we simply do -->
# --> Cos(Angle between both vectors) = (a . b) / |a|*|b| where |a| aka Vector Length simply means sqrt(a1**2, a2**2, a3**2)
#
# Notes: Cross Product
# If we have 2 vectors a = <1, 3, 4> and b = <2, 7, -5> Then the cross product will be -->
# --> where a = i + 3j + 4k and b = 2i + 7j - 5k -->
#
# -->         [i  j  k]
# --> a X b = [1  3  4] = i * [3  4] - j * [1  4] + k * [1  3]  = i(-15 - 28) - j(-5 - 8) + k(7 - 6) = -43 * i + 13 * j + k * 1 -->
# -->         [2  7 -5]       [7 -5]       [2 -5]       [2  7]
#
#--> which is a vector of the lengths <-43i, 13j, k> and is orthogonal to the other two vectors