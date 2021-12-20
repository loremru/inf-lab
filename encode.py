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

def convert_base_decimal(num, base):
    from decimal import Decimal
    import math
    al = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = '0.'
    f = []
    m = []
    prev_f = None
    while num>0:
        num = Decimal(str(base))*Decimal(str(num))
        f.append(num)
        if prev_f in f[:-2]:
            k = f[:-2].index(prev_f)
            if f[k+1] == num:
                for i in range (k):
                    res += m[i]
                res += '('
                for i in range(k,len(m)-1):
                    res += m[i]
                res += ')'
                break
        prev_f = num
        if math.floor(num)<10:
            m.append(str(math.floor(num)))
        else:
            m.append(al[math.floor(num)])
        num = Decimal(str(num))- Decimal(str(math.floor(num)))
    return res

def to_ternary(num: int):
    cur_num = num
    arr = []
    while True:
        res = cur_num // 3
        temp = cur_num % 3
        cur_num = res

        if temp == 2:
            arr.append('#')
            res += 1
            cur_num = res
        if temp != 2:
            arr.append(str(temp))
        if res < 3:
            if res == 2:
                arr.append('#')
                arr.append('1')
            if res == 1:
                arr.append('1')
            break
    return "".join(arr[::-1])

def make_answer(arr):
    answer = ""
    temp_length = 20
    i = 0
    is_reverse = False
    while True:
        if i == 4:
            i -= 1
            is_reverse = True
        elif i == 0:
            is_reverse = False
        if temp_length > 0:
            new_range = range(len(arr[i]) -1, -1, -1) if is_reverse else range(len(arr[i]))
            for j in new_range:
                if temp_length > 0:
                    item = arr[i][j]
                    answer += item
                    temp_length -= 1
                else:
                    break
            i += -1 if is_reverse else 1
        else:
            break
    return answer

def encode_word(word: str):
    encoded_letters = []
    for i in word:
        encoded_num = letter_dir[i.upper()]
        encoded_letters.append(encoded_num)
    a = convert_base(encoded_letters[0], encoded_letters[1])
    b = convert_base_decimal(encoded_letters[2]/10**len(str(encoded_letters[2])),encoded_letters[3]).replace(')', '').replace('(', '').replace('0.', '')
    # c = to_ternary(encoded_letters[1])
    # d = to_ternary(encoded_letters[3])
    # new_arr = [a, c, b, d]
    return [a,b]  # Тут возвращать закодированное слово
