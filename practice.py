#


def main():
    value = input("enter number in meters ")
    if value is not float:
        print("invalid")
    else:
        cm = float(value) / 100
        print("The value you entered in meters is equal to ", cm ,"centimeters")

main()
