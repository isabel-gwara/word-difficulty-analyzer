import csv
import string

filename = input("Enter the name of the file you would like to read...")

words = set()

# estimated words known
four_year_old = 5000
eight_year_old = 10000
high_schooler = 15000
lower_adult = 20000
higher_adult = 35000

with open('unigram_freq.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    counter = 0

    for row in csv_reader:
        if counter >= high_schooler:
            break
        words.add(row[0])
        counter += 1

with open(filename, 'r', encoding="utf8") as text_file:
    for line in text_file:
        for word in line.split():
            transformed_word = word.lower().translate(str.maketrans('', '', string.punctuation))
            if transformed_word not in words:
                print(transformed_word)

# write a section that replaces the word with X's based on how long it is, then saves or outputs the text