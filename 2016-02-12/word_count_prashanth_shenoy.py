import os, sys

def start ():
    input_file_obj = open ('input_file.txt', 'r')
    word_list = input_file_obj.read ().split()
    print "There are a total of %d words" % len(word_list)

    word_repetition_dict = {}
    for word in word_list:
        try:
            word_repetition_dict [word] = word_repetition_dict [word] +1
        except KeyError:
            word_repetition_dict [word] = 1

    #for (word, word_count) in word_repetition_dict.items():
    #    print "%s \t\t %d" % (word, word_count)

    for (word, word_count) in sorted (word_repetition_dict.items(), key= lambda x: x[1], reverse=True):
        print "%s \t\t %d" % (word, word_count)

if __name__ == "__main__":
	start()
	sys.exit(0)
