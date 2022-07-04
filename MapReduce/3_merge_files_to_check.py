import os

filename = "moscow.txt"

counts = dict()

def count_words(filename):

    text = open(filename)

    for line in text:
        line = line.strip()
        line = line.lower()

        words = line.split(":")
        word = words[0].strip()
        count = int(words[1])

        if word in counts:
            counts[word] = counts[word] + count
        else:
            counts[word] = count

# count_words(filename)

import glob

# absolute path to search all text files inside a specific folder
path = r'moscow_out*'
files = glob.glob(path)
print(files)

for filename in files:
    count_words(filename)

# for word, count in counts.items():
#     print(word, ":", count)

for word, count in dict(sorted(counts.items())).items():
    print(word, ":", count)

#
# sorted_dict = {}
# sorted_keys = sorted(counts, key=counts.get, reverse=True)
#
# for w in sorted_keys:
#     sorted_dict[w] = counts[w]
#
# print("words : ", len(counts))
#
# for word, count in sorted_dict.items():
#     print(word, ":", count)