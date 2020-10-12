#!/usr/local/bin/python3
from string import punctuation


STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were', 'will', 'with'
}


def format_word_freq(wf):
    """
    Return a string of the word frequency dictionary wf formatted for printing.
    """
    format_width = max(len(w) for w in wf)
    output_string = ""

    for w in sorted(wf, key=wf.get, reverse=True):
        count = wf[w]
        output_string += f"{w:>{format_width}} : {count} {'*' * count}\n"

    return output_string


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    # Step 1: read the contents of the file
    with open(file) as wordsfile:
        words = wordsfile.read()

    # print("After Step 1:")
    # print(words)

    # Step 2: convert the contents of the file to lowercase
    words = words.lower()

    # print("After Step 2:")
    # print(words)

    # Step 3: remove punctuation

    # Step 3a: iterate through all the punctuation characters
    for p in punctuation:
        # Step 3b: remove the punctuation character from words and reassign words
        words = words.replace(p, '')

    # print("After step 3:")
    # print(words)

    # Step 4: break the file contents into words
    wordslist = words.split()

    # print("After step 4:")
    # print(wordslist)

    # Step 5: Remove words from the list STOP_WORDS
    for s_w in STOP_WORDS:
        while s_w in wordslist:
            wordslist.remove(s_w)

    # print("After step 5:")
    # print(wordslist)

    # Step 6: Iterate through wordslist and count occurrences of each word
    # Step 6a: create a dictionary to hold word counts
    wordscounts = {}

    # Step 6b: iterate through the words in wordslist
    for w in wordslist:
        # Step 6c: check if w has already been seen
        if w in wordscounts:
            # Step 6cA: if it has, add 1 to the count
            wordscounts[w] += 1

        else:
            # Step 6cB: if it hasn't, set the count to 1
            wordscounts[w] = 1

    # An alternative way to do the steps above
    # for w in wordslist:
    #    if w not in wordscounts:
    #        wordscounts[w] = 0

    #    wordscounts[w] += 1

    # Another alternative way to do the steps above
    # from collections import Counter
    # wordscounts = Counter(wordslist)

    # print("After step 6:")
    # print(wordscounts)

    # Step 7: get formatted output and print it
    formatted = format_word_freq(wordscounts)
    print(formatted)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
