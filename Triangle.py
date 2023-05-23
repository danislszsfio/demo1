def main():
    lst = []
    for i in range (0,3):
        n = float(input("Plug in a value"))
        if n <= 0:
            print("Plug in positive values")
        else:
            lst.append(n)
    print (lst)
    if lst[0] == lst[1] == lst[2]:
        print("your triangle is equilateral")
    elif lst[0] == lst[1] and lst[0] != lst[2] or lst[0] == lst[2] and lst[0] != lst[1] or lst[1] != lst[1] and lst[1] == lst[2]:
        print("Your triangle is isosceles")
    else:
        print("Your triangle is shit")

main()