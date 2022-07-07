from output import *

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


def count_words(text):
    global counts

    text = open("everest.txt")

    for line in text:
        words = get_words(line)

        for word in words:
            if written_in_english(word):
                if word in counts:
                    counts[word] = counts[word] + 1
                else:
                    counts[word] = 1


if __name__ == "__main__":
    filename = "everest.txt"
    count_words(filename)
    output_alphabetically(counts)
