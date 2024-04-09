def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        print("List is empty. Cannot calculate average.")
        return None
    average = total / count
    return average

numbers = []
for i in range(3):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

average = calculate_average(numbers)
if average is not None:
    if average > 50:
        print("You have exceeded 50 with an average of", average)
    else:
        print("Your average is", average)

