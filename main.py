import numpy as np

# 1. Створення двовимірного масиву 3x3 з випадкових цілих чисел від 1 до 100
array = np.random.randint(1, 101, size=(3, 3))
print("Початковий масив:\n", array)

# 2. Обчислення суми всіх елементів масиву
total_sum = np.sum(array)
print(f"\nСума всіх елементів: {total_sum}")

# 3. Знаходження максимального та мінімального значень та їхніх індексів
max_val = np.max(array)
min_val = np.min(array)

max_idx = np.unravel_index(np.argmax(array), array.shape)
min_idx = np.unravel_index(np.argmin(array), array.shape)

max_idx_clean = tuple(map(int, max_idx))
min_idx_clean = tuple(map(int, min_idx))

print(f"Максимальне значення: {max_val}, індекс: {max_idx_clean}")
print(f"Мінімальне значення: {min_val}, індекс: {min_idx_clean}")

# 4. Сортування масиву по кожному рядку
sorted_array = np.sort(array, axis=1)
print("\nВідсортований масив (по рядках):\n", sorted_array)