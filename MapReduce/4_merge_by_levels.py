
import os
import glob

filename = "moscow.txt"

counts = dict()
depth_step = 40
start_depth_level = 0
end_depth_level = depth_step
file_number = 0
max_words_in_ram = 510


def save_to_file():
    global start_deep_level
    global end_deep_level
    global counts
    global file_number
    output_file = filename.split("_")[0] + "_depth" + "_" + str(start_depth_level) + "-" + str(end_depth_level) + ".txt" #  + "_" + str(file_number) + ".txt"
    with open(output_file, 'w') as f:
        for word, count in dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)).items():
            f.write('%s : %s\n' % (word, count))

        # for word, count in sorted(counts.items()): # , reverse=True # sort by key
        #     f.write('%s : %s\n' % (word, count))

    file_number = file_number + 1


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



# absolute path to search all text files inside a specific folder
path = r'moscow_out*'
files = glob.glob(path)
print(files)

while end_depth_level < max_words_in_ram:
    for filename in files:
        count_words(filename)

    save_to_file()
    start_depth_level = start_depth_level + depth_step
    end_depth_level = end_depth_level + depth_step
    counts.clear()

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