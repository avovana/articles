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


text = open("moscow.txt")
counts = dict()


def count_words(text):
    global counts

    for line in text:
        words = get_words(line)

        for word in words:
            if written_in_english(word):
                if word in counts:
                    counts[word] = counts[word] + 1
                else:
                    counts[word] = 1

count_words(text)

# for word, count in counts.items():
#     print(word, ":", count)

# for word, count in dict(sorted(counts.items())).items():
#     print(word, ":", count)


sorted_dict = {}
sorted_keys = sorted(counts, key=counts.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = counts[w]

print("words : ", len(counts))

for word, count in sorted_dict.items():
    print(word, ":", count)
