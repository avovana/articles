# -*- coding: utf-8 -*-

import glob
import math
import argparse
import sys


counts = dict()


def save_to_file(start_depth_level, end_depth_level, filename):
    # global counts
    output_file = filename.split("_")[0] + "_depth_third" + "_" + str(start_depth_level) + "-" + str(end_depth_level) + ".txt" #  + "_" + str(file_number) + ".txt"
    with open(output_file, 'w') as f:
         for word, count in sorted(counts.items()): # , reverse=True # sort by key
             f.write('%s : %s\n' % (word, count))

        # for word, count in dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)).items():
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='script merges word pairs from different files')
    parser.add_argument('input_files_mask', type=str, help='A files mask to merge files')
    args = parser.parse_args()

    files_mask = args.input_files_mask

    files = glob.glob(files_mask)   # print(files)

    max_words_in_ram = 500
    depth_step = math.floor(max_words_in_ram / len(files))

    start_depth_level = 0
    end_depth_level = depth_step

    while end_depth_level < max_words_in_ram:
        for filename in files:
            count_words(filename)

        save_to_file(start_depth_level, end_depth_level, filename)
        start_depth_level = start_depth_level + depth_step
        end_depth_level = end_depth_level + depth_step
        counts.clear()

    sys.exit(1)