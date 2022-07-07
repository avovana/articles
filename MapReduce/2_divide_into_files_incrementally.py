# -*- coding: utf-8 -*-

import os


max_words_in_ram = 500
current_words_quantity = 0
counts = dict()


def written_in_english(word):
    try:
        word.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        if word.isalpha():
            return True
        else:
            return False


def get_words(line):
    line = line.strip()
    line = line.lower()
    words = line.split()

    return words


def save_to_file(counts, exceed_ram_times):
    output_file = os.path.splitext(filename)[0] + "_out" + str(exceed_ram_times) + ".txt"
    with open(output_file, 'w') as f:
        for word, count in dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)).items():
            f.write('%s : %s\n' % (word, count))

        # for word, count in sorted(counts.items()): # , reverse=True
        #     f.write('%s : %s\n' % (word, count))


def count_words(filename):
    global counts
    global max_words_in_ram
    global current_words_quantity

    exceed_ram_times = 0

    text = open(filename)

    for line in text:
        words = get_words(line)

        for word in words:
            if written_in_english(word):
                if word in counts:
                    counts[word] = counts[word] + 1
                else:
                    counts[word] = 1
                    if current_words_quantity < max_words_in_ram:
                        current_words_quantity = current_words_quantity + 1
                    else:
                        exceed_ram_times = exceed_ram_times + 1
                        current_words_quantity = 0

                        save_to_file(counts, exceed_ram_times)
                        counts.clear()

    exceed_ram_times = exceed_ram_times + 1
    save_to_file(counts, exceed_ram_times)
    counts.clear()


if __name__ == "__main__":
    filename = "everest.txt"
    count_words(filename)
