numbers = []
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    numbers.append(num)
    num = int(input("ENter a number (0 to stop): "))

print(f"\nNumbers entered: {numbers}")

highest = max(numbers)
lowest = min(numbers)

range_value = highest - lowest

print(f"The highest number is: {highest}")
print(f"The lowest number is: {lowest}")
print(f"The range is: {range_value}")
