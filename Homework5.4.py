
rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

with open('test-21.txt', 'w') as write_file:
    with open('test-2.txt', 'r') as read_file:

        for line in read_file:
            line_split = line.split(" ")

            line_translated = []

            for word in line_split:
                if word.lower() in rus_dict.keys():
                    line_translated.append(rus_dict[word.lower()])
                else:
                    line_translated.append(word)

            line_translated = " ".join(line_translated)

            write_file.write(line_translated)





