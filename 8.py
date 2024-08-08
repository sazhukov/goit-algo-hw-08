import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    # Ініціалізація мінімальної купи
    heapq.heapify(cable_lengths)

    total_cost = 0

    # Об'єднання кабелів, поки в купі більше одного кабеля
    while len(cable_lengths) > 1:
        # Витягуємо два найменших кабелі
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)

        # Об'єднуємо кабелі та додаємо вартість об'єднання до загальних витрат
        combined_length = first_min + second_min
        total_cost += combined_length

        # Додаємо новий об'єднаний кабель до купи
        heapq.heappush(cable_lengths, combined_length)

    # Повертаємо загальні витрати
    return total_cost

if __name__ == '__main__':
    # Приклад використання
    cable_lengths = [1, 3, 9, 2, 1, 2]

    print(sorted(cable_lengths))

    print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
