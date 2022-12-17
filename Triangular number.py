def triangular_number(x):
    from math import sqrt as radikal
    # x=int(input("enter the numer ..."))
    x_new = (2*x)
    a = 1
    b = 1
    c = -(x_new)
    delta = (b**2 - (4*a*c))
    if delta > 0:
        x1 = (-b + (radikal(delta)))/2*a
        x2 = (-b - (radikal(delta)))/2*a
    if x1 == int(x1) and x2 == int(x2):
        print(f"{x}=True")
    else:
        print(f"{x}=False")
triangular_number(3)
