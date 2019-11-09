#square, circle, trapezium, triangle

def square_field(a):
    field = a **2
    return(field)

def circle_field(r):
    pi = 3.14
    field = pi * (r**2)
    return(field)

def trapezium_field(a,b, h):
    field = ((a + b)/2)*h
    return(field)

def triangle_field(a,h):
    field = (a*h)/2
    return(field)

