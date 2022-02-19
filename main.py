from math import sqrt

def solvePoly(a, b, c):
  delta = b**2 - 4*a*c
  if (delta > 0):
    x1 = (-b + sqrt(delta))/ 2*a
    x2 = (-b - sqrt(delta))/ 2*a
    return [x1, x2]
  elif (delta == 0):
    x = - b /2*a 
    return x
  else :
    return "no solution In R"

a = int(input("enter a\n"))
b = int(input("enter b\n"))
c = int(input("enter c\n"))


solution = solvePoly(a , b , c)
print(solution)
