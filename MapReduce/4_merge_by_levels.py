# -*- coding: utf-8 -*-

import glob
import math
import argparse
import sys


max_words_in_ram = 500
counts = dict()


def save_to_file(start_depth_level, end_depth_level, filename, output_file_postfix):
    # global counts
    output_file = filename.split("_")[0] + "_" + output_file_postfix + "_" + str(start_depth_level) + "-" + str(end_depth_level) + ".txt" #  + "_" + str(file_number) + ".txt"
    with open(output_file, 'w') as f:
         for word, count in sorted(counts.items()):
             f.write('%s : %s\n' % (word, count))


def count_words(filename, start_depth_level, end_depth_level):
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


def merge_files_by_levels(files, output_file_postfix):
    depth_step = math.floor(max_words_in_ram / len(files))

    start_depth_level = 0
    end_depth_level = depth_step

    while end_depth_level < max_words_in_ram:
        for filename in files:
            count_words(filename, start_depth_level, end_depth_level)

        save_to_file(start_depth_level, end_depth_level, filename, output_file_postfix)
        start_depth_level = start_depth_level + depth_step
        end_depth_level = end_depth_level + depth_step
        counts.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='script merges word pairs from different files')
    parser.add_argument('input_files_mask', type=str, help='A files mask to merge files')
    parser.add_argument('output_file_postfix', type=str, help='A postfix to identify output file based on input file')
    args = parser.parse_args()

    files_mask = args.input_files_mask
    output_file_postfix = args.output_file_postfix
    files = glob.glob(files_mask)

    merge_files_by_levels(files, output_file_postfix)

    sys.exit(1)