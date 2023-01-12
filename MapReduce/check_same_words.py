import os
import subprocess
import glob
import argparse
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_files_paires(files):
	pairs = list()
	cache = list()

	for file in files:
	    for other_file in files:
	        if file is other_file:
	            continue
	        
	        pair = tuple()

	        if file > other_file:
	            pair = (other_file, file)
	        else:
	            pair = (file, other_file)

	        if pair not in cache:
	            cache.append(pair)
	            pairs.append(pair)

	return pairs

def print_matched_words(pairs):
	for file1_name, file2_name in pairs:

		header_printed = False
		with open(file1_name) as file1:
			word1 = ''
			for num1, line1 in enumerate(file1, 1):
				word1 = line1.partition(' ')[0]
				
				with open(file2_name) as file2:
					for num2, line2 in enumerate(file2, 1):
						if word1 == line2.partition(' ')[0]:
							if not header_printed:
								header_printed = True
								header = '{:<12}  {:^22}  {:^22}'.format("match word", file1_name, file2_name)
								print(header) # print(bcolors.HEADER + header + bcolors.ENDC)

							line = '{:<12}  {:^22}  {:^22}'.format(word1, num1, num2)
							print(line) # print(bcolors.OKGREEN + line + bcolors.ENDC)

	return 1


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='script looks for the same words in files')
	parser.add_argument('input_files_mask', type=str, help='A files mask to make paired files')
	args = parser.parse_args()

	files_mask = args.input_files_mask
	files = glob.glob(files_mask)

	files_pairs = get_files_paires(files)
	res = print_matched_words(files_pairs)
	sys.exit(1)