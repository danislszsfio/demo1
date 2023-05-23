def main():
    added = 0
    i = 0
    x = 0
    while x != "":
        x = (input("Enter a number"))
        try:
            added = added + float(x)
            i += 1
        except:
            print("ERROR")
        print(f"{added=} {x=} {i=}")
    print("This is your average",added/i)
main()