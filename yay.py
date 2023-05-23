import math

def main():
    print("this program calculates the solutions to a quadratic")
    print()
    a = float(input("enter coefficient a:"))
    b = float(input("enter coefficient b"))
    c = float(input("enter coefficient c"))
    discRoot = math.sqrt(b**2-4*a*c)
    root1 = (-b+discRoot)/(2*a)
    root2 = (-b - discRoot) / (2 * a)
    print("the solution are:",round(root1,2), round(root2,2))
main()