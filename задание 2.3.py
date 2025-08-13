
def average(numbers):
    if not numbers:
        return 0  # или можно вернуть None, если список пуст
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40]
result = average(nums)
print("Среднее значение:", result)