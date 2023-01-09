import os
import subprocess

# bashCommand = "grep -wFf everest_depth_0-33.txt everest_depth_33-66.txt > output.log"

import glob

files = glob.glob('everest_depth*.txt')

print(type(files))

res = list()
print(type(res))
print(res)

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
            res.append(pair)

print(res)

for file1, file2 in res:
	# process = subprocess.Popen(["awk", "FNR==NR{a[$3];x=1; next} ($3 in a){delete a[$3]; print x  \" : \" $3 ; x += 1}", file1, file2], stdout=subprocess.PIPE)
	process = subprocess.Popen(["awk", "NR==FNR{a[$1];next} $1 in a {print FNR \" : \" $1 }", file1, file2], stdout=subprocess.PIPE)


	output, error = process.communicate()
	output = output.decode("utf-8")
	print(file1 + " " + file2)
	print(output)
	# print(error)

	# dir_path = os.path.dirname(os.path.realpath(__file__))
	# subprocess.call('ls')
	#subprocess.call("") #  grep -wFf everest_depth_0-33.txt everest_depth_33-66.txt
