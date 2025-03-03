numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]


def first_uppercase(text):
    return text[0].isupper() if text else False
print(first_uppercase("I love You"))   # ➝ 'I'