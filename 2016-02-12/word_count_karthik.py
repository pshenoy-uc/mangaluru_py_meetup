"""
__author__ : K@rthik
__date__ : Mar 12, 2016
"""
# re is a regular expression module
import re
import time
# Counter is a high performace datatype from collections module
from collections import Counter 

total_words = 0
word_counter = Counter()
# Open file with read mode and read the file
with open("input_file.txt") as file_handle:
	file_content = file_handle.read()

start_time = time.clock()
# Split the entire file content by space, tab or newline.
words = re.split(r"\s|\t|\n", file_content)
for word in words:
	word = word.strip()

	# If word is not an empty string or None then we check if word is present in the
	# counter dictionary.
	if word:
		# if word is already present the counter gets incremented
		# if word is not present in the dict then it is set to 1.
		word_counter[word] += 1
		total_words += 1

counter_dict = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
total_time = time.clock() - start_time

# Open file with write mode and write to the file.
with open("output_karthik.txt", "w") as output_file:
	output_file.write("There are {0} number of words in the file.\nTime taken to execute script: {1} seconds\n".format(total_words, total_time))
	for word, frequency in counter_dict:
		output_file.write("{word}: {frequency}\n".format(word=word, frequency=frequency))

# End of file
