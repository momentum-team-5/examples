#!/usr/local/bin/python3
from string import punctuation


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were', 'will', 'with'
]


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
    wordslist = [w for w in words.split() if w not in STOP_WORDS]
    wordscounts = {w: wordslist.count(w) for w in set(wordslist)}

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
