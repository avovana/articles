import glob
import math

counts = dict()


def save_to_file(start_depth_level, end_depth_level, filename, file_number):
    global counts
    output_file = filename.split("_")[0] + "_depth" + "_" + str(start_depth_level) + "-" + str(end_depth_level) + ".txt" #  + "_" + str(file_number) + ".txt"
    with open(output_file, 'w') as f:
        for word, count in dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)).items():
            f.write('%s : %s\n' % (word, count))

        # for word, count in sorted(counts.items()): # , reverse=True # sort by key
        #     f.write('%s : %s\n' % (word, count))


def count_words(filename):
    global counts
    text = open(filename)

    for i, line in enumerate(text):
        if not(start_depth_level <= i < end_depth_level):
            continue

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


if __name__ == "__main__":
    # absolute path to search all text files inside a specific folder
    path = r'moscow_out*'
    files = glob.glob(path)
    print(files)

    file_number = 0
    max_words_in_ram = 500
    depth_step = math.floor(max_words_in_ram / len(files))

    filename = "moscow.txt"

    start_depth_level = 0
    end_depth_level = depth_step

    while end_depth_level < max_words_in_ram:
        for filename in files:
            count_words(filename)

        save_to_file(start_depth_level, end_depth_level, filename, file_number)
        start_depth_level = start_depth_level + depth_step
        end_depth_level = end_depth_level + depth_step
        counts.clear()
        file_number = file_number + 1

    #
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