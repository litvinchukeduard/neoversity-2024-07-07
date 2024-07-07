import re
'''
Написати функцію, яка буде приймати текст і список зі спам-слів. І буде з 
цього тексту прибирати спам-слова та ставити замість них зірочки
'''

text = """
PyТhON is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[34][35]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] PyThON 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.
"""

{
    't': 'т'
}

def replace_spam_words(text: str, spam_words: list[str]) -> str:
    for word in spam_words:
        pattern = fr'\b{word}\b'
        replace_string = '*' * len(word)
        text = re.sub(pattern, replace_string, text, flags=re.IGNORECASE)
    return text

print(replace_spam_words(text, ['Python', 'Rossum']))
print('123' * 4)
