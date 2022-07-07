import glob
from output import *

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


if __name__ == "__main__":
    filename = "everest.txt"
    files_mask = filename.split(".")[0] + "_out*"
    files = glob.glob(files_mask)  # print(files)

    for filename in files:
        count_words(filename)

    output_alphabetically()
