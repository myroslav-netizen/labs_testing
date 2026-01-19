def calculate_average(numbers: list):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
