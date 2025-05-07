import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.a = real
        self.b = imaginary
    def __add__(self, no):
        operator = "+"
        if (self.b + no.b) < 0:
            operator = ""
        return str(f"{(self.a + no.a):.2f}") + operator + str(f"{(self.b + no.b):.2f}") + "i"
    def __sub__(self, no):
        operator = "+"
        if (self.b - no.b) < 0:
            operator = ""
        return str(f"{(self.a - no.a):.2f}") + operator + str(f"{(self.b - no.b):.2f}") + "i"
    def __mul__(self, no):
        a = (self.a * no.a)
        b = (self.a * no.b)
        c = (self.b * no.a)
        d = (self.b * no.b) * -1
        e = a + d
        f = b + c
        operator = "+"
        if (f) < 0:
            operator = ""
        return (str(f"{(e):.2f}") + operator + str(f"{(f):.2f}")) + "i"
    def __truediv__(self, no):
        a = (self.a * no.a)
        b = (self.a * -(no.b))
        c = (self.b * no.a)
        d = (self.b * -(no.b)) * -1
        e = (no.a  * no.a)
        f = (no.a  * -(no.b))
        g = (no.b * no.a)
        h = (no.b * -(no.b)) * -1
        i = a + d
        j =  b + c
        k = e + h
        l = f + g
        m = str(f"{(i / k):.2f}")
        n = str(f"{(j / k):.2f}")
        operator = "+"
        if (j / k) < 0:
            operator = ""
        return m + operator + n + "i"
    
    def mod(self):
        return str(f"{(math.sqrt(self.a**2 + self.b**2)):.2f}") + "+0.00i"

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')



# Notes: Imaginary numbers 
# i = sqrt(-1) Therefore i is imaginary, There are expressions with i that are indeed real numbers.
# Ex. i**2 = sqrt(-1) * sqrt(-1) = -1
# Ex. i**3 = -1 * i = -i
# Ex. i**4 = i**2 * i**2
# Ex. i**5 = i
# EX. The cycle repeats every increment of 4 on the exponent

# Lets say i = sqrt(-9) which equals sqrt(9) * sqrt(-1) = 3*i
# Therefore the sqrt(-x) will always be i * sqrt(x)

# Notes: Complex Numbers
# Anytime we have real numbers combined with imaginary numbers Ex. a + b*i (where a is a real number and b*i is i * sqrt(x) imaginary number) ->
# -> we call it a complex number
# Rule: All numbers are complex numbers, real numbers just have b = 0
# Rule: If a is zero, we have a pure imaginary number
# Rule: If a and b are both not zero, we have complex number
# Addition: 
# Ex. (2 + i) + (3 - 2*i) = 5 - i
# Multiplication / Division:
# Ex. (2 - i) * (4 + 2*i) = 8 + 4*i - 4*i - 2*i^2  =  8 - 2*i^2  =  8 - 2*-1 = 10
# (5 + 2*i) / (3 - i) = ((5 + 2*i) * (3 + i)) / ((3 - i) * (3 + i)) = (15 + 5*i + 6i + 2*i^2) / (9 + 3i - 3i - i^2) = (13 + ll*i) / (9 - i^2) = (13 + 11*i) / 10 = (13/10) + ((11*i)/10)





