'''
Написати функцію, яка буде приймати рядок та повертати список слів у цьому рядку
'''
import re

# "Hello, world, hElLo!" -> ['Hello', 'world'] -> ['hello', 'world']

def split_sentence_into_words_split(sentence: str) -> list[str]:
    # pattern = r'[a-zA-Z]+'
    pattern = r'[!, ]+\b'
    return re.split(pattern, sentence)

def split_sentence_into_words_findall(sentence: str) -> list[str]:
    pattern = r'[a-zA-Z]+'
    # pattern = r'[!, ]+\b'
    words = re.findall(pattern, sentence)
    result_words = list() #[] 

    # my_dict = {}

    for word in words:
        result_words.append(word.lower())
    return result_words

print(split_sentence_into_words_split("Hello, world, hElLo!"))
print(split_sentence_into_words_findall("Hello, world, hElLo!"))

# my_dict = set() dict()
# print(type(my_dict))
