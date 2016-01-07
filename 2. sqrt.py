__author__ = 'Mj'
num = input('Number? ')
nom = float(num)

if nom < 0:
    print("Number must be positive only")
    exit()
elif nom < 1:
    lower = float(nom)
    upper = 1
else :
    lower = 0.0
    upper = float(nom)
tolerance = -1.0
while tolerance <= 0:
    tol = input("Enter tolerance allowed: ")
    tolerance = float(tol)

uncertainity = upper - lower
while uncertainity > tolerance:
    middle = (upper + lower)/2
    if middle**2 < float(nom) :
        lower = middle
    else :
        upper = middle
    uncertainity = upper - lower
    print( upper, lower, middle**2)
