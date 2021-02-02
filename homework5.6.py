
hours_dict = {}

with open('test-4.txt', 'r') as my_file:

    for line in my_file:


        line_another_split = line.split(":")

        subject = line_another_split[0]

        sum = 0

        other_words = line_another_split[1:]
        other_words = other_words[0].split(" ")

        for word in other_words:

            integers = [s for s in list(word) if s.isdigit()]

            if integers != []:

                integers_string = "".join(integers)
                integers_number = int(integers_string)

                sum += integers_number

        hours_dict[subject] = sum


for key, value in hours_dict.items():
    print(f"{key} : {value}")
