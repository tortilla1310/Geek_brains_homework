def int_func(word):
    phrase_up = word.title()
    return phrase_up


words = input('Введите слово с маленькой латинской буквы\n')
words_list = words.strip().split(" ")

words_capitalized=[]
for word in words_list:
    words_capitalized.append(int_func(word))

# words_capitalized = [int_func(word) for word in words_list]


print(" ".join(words_capitalized))

