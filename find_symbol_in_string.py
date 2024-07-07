'''
Написати функцію, яка буде у рядку шукати сивол та повертати його індекс
'''

[1, 2, 3, 4]
"Hello, world"

def find_symbol_in_string(text: str, symbol: str) -> int:
    return text.find(symbol)

def find_symbol_in_string_my_implementation(text: str, symbol: str) -> int:
    # Forth
    index = 0
    for char in text:
        if char == symbol:
            return index
        index += 1
    return -1


print(find_symbol_in_string("Hello, world", "w"))
print(find_symbol_in_string_my_implementation("Hello, world", "H"))


# def find_symbol_in_string_my_implementation(text: str, symbol: str) -> int:
    # First
    # for char in text:
    #     if char == symbol:
    #         print(char)
    #         return text.index(char)

    # Second
    # for i in range(len(text)):
    #     if text[i] == symbol:
    #         return i

    # Third
    # for index, char in enumerate(text):
    #     if char == symbol:
    #         return index