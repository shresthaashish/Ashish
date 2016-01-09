#!/usr/bin/env python

'''This script  find all of the anagrams in a dictionary
 in which there are at least 4 letters in the word and
 atleast as many anagrams as there are letters.'''

import sys
from collections import defaultdict


def load_dictionary(dict_location):
    try:
        with open(dict_location) as w:
            for word_list in w:
                yield word_list.rstrip()
    except:
        print("file does not exist")
        sys.exit(0)


def find_anagram(dictionary):
    data = defaultdict(list)
    for word in dictionary:
        key = "".join(sorted(word))
        if len(key) >= 4:
            data[key].append(word)
    for key, ana in data.items():
        if len(ana) >= len(key):
            print ", ".join(ana)


def main():
	dict_location = '/usr/share/dict/words'
	dictionary = load_dictionary(dict_location)
	find_anagram(dictionary)


if __name__ == "__main__":
	main()
