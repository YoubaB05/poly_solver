from math import sqrt

def solvePoly(a, b, c):
    delta = b**2 - 4 * a * c
    if (delta > 0):
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f'This equation accepts two solutions: {x1}, {x2}')

    elif (delta == 0):
        x = -b / (2*a)
        print(f'This equation accepts one solution: {x}')
    else:
        print("This equation accepts no solution In R")




def solver():
  a = int(input("enter a\n"))
  b = int(input("enter b\n"))
  c = int(input("enter c\n"))  
  
  
  solvePoly(a, b, c)
  choice = input("\nDo you want to try again? (Y/N)\n")
  if(choice == "Y" or choice == "y"):
    solver()
  else:
    print("Bye!")
    exit()


solver()





