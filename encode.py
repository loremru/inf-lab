letter_dir = {"А": 1, "Б": 2, "В": 3, "Г": 4, "Д": 5, "Е": 6, "Ж": 7, "З": 8, "И": 9, "Й": 10, "К": 11, "Л": 12, "М": 13, "Н": 14, "О": 15, "П": 16, "Р": 17, "С": 18, "Т": 19, "У": 20, "Ф": 21, "Х": 22, "Ц": 23, "Ч": 24, "Ш": 25, "Щ": 26, "Ъ": 27, "Ы": 28, "Ь": 29, "Э": 30, "Ю": 31, "Я": 32 }


def encode_word(word: str):
    encoded_letters = []
    for i in word:
        encoded_num = letter_dir[i.upper()]
        encoded_letters.append(encoded_num)
    return encoded_letters  # Тут возвращать закодированное слово
