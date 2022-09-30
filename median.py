"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    """Median calculator."""
    """ENTER YOUR SOLUTION HERE!"""
    while True:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
            numbers.sort()

            evenOrNot = len(numbers) % 2
            medianIndex = 0
            median = 0

            if evenOrNot == 1:
                medianIndex = (len(numbers) - 1)/2
                median = numbers[int(medianIndex)]
                print(median)
            else:
                medianIndex = (len(numbers))/2
                median1 = numbers[int(medianIndex)]
                median2 = numbers[int(medianIndex - 1)]
                median3 = (median1 + median2)/2
                print(median3)
        except ValueError:
            print("Some input could not be converted to a number!")
        else:
            break
print(numbers)
