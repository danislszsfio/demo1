def main():
	numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").strip().split() if x.isdigit()]
	average = sum(numbers) / len(numbers)
	print("The average is: ", average)
main()