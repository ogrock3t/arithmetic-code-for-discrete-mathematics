def arithmetic_code(freq):
    sum_freq = sum(freq)
    probabilities = [f / sum_freq for f in freq]

    intervals = []
    low = 0.0
    for prob in probabilities:
        high = low + prob
        intervals.append((low, high))
        low = high

    low, high = 0.0, 1.0
    for char in text:
        index = russian_alphabet.index(char)
        symbol_low, symbol_high = intervals[index]
        range_width = high - low
        high = low + range_width * symbol_high
        low = low + range_width * symbol_low

    return (low + high) / 2, intervals, (low, high)


if __name__ == "__main__":
    text = input("Введите слово, которое нужно закодировать: ")
    text = text.upper()
    russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    freq_letter = [0] * 33

    for char in text:
        index = russian_alphabet.index(char)
        freq_letter[index] += 1

    result, intervals, final_interval = arithmetic_code(freq_letter)

    print(f"Закодированное значение: {result}")
    print(f"Финальный интервал: {final_interval}")

    print("Таблица интервалов:")
    for i, interval in enumerate(intervals):
        if freq_letter[i] > 0:
            print(f"{russian_alphabet[i]}: {interval}")

    print("Частота букв в тексте:")
    for i in range(33):
        if freq_letter[i] > 0:
            print(f"{russian_alphabet[i]}:  {freq_letter[i]}")
