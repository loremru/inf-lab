letter_dir = {"А": 1, "Б": 2, "В": 3, "Г": 4, "Д": 5, "Е": 6, "Ж": 7, "З": 8, "И": 9, "Й": 10, "К": 11, "Л": 12, "М": 13, "Н": 14, "О": 15, "П": 16, "Р": 17, "С": 18, "Т": 19, "У": 20, "Ф": 21, "Х": 22, "Ц": 23, "Ч": 24, "Ш": 25, "Щ": 26, "Ъ": 27, "Ы": 28, "Ь": 29, "Э": 30, "Ю": 31, "Я": 32 }


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

# def translate_digit(num, n):
#     str_digits = ""
#     while num:
#         digit = num % n
#         str_digits += str(digit)
#         num //= n
#     return str_digits[:: -1]


def encode_word(word: str):
    encoded_letters = []
    for i in word:
        encoded_num = letter_dir[i.upper()]
        encoded_letters.append(encoded_num)

    # Тут возвращать закодированное слово
    return convert_base(float("0." + str(encoded_letters[2])), encoded_letters[3])
