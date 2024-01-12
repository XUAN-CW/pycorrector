# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys

from pycorrector.macbert.macbert_corrector import MacBertCorrector

sys.path.append(".")
from pycorrector import Corrector


def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    return lines


def print_with_red_segments(text, segments):
    # ANSI escape codes for colors
    RED = '\033[91m'
    BLACK = '\033[0m'

    last_index = 0
    result = ""

    # Sort segments by start_index
    segments.sort(key=lambda x: x[0])

    # Process each segment
    for start_index, length in segments:
        # Ensure start_index and length are within the bounds of the string
        start_index = max(0, min(start_index, len(text)))
        end_index = max(start_index, min(start_index + length, len(text)))

        # Append non-red and red parts to result
        result += text[last_index:start_index] + RED + text[start_index:end_index] + BLACK

        last_index = end_index

    # Append any remaining part of the string after the last segment
    result += text[last_index:]

    # Print the result
    print(result)

nameList = {"阳大根"}


def isInNameList(source,startIndex):
    for name in nameList:
        error = source[startIndex:startIndex+len(name)]
        if error == name:
            return True

if __name__ == '__main__':
    m = MacBertCorrector()
    # m = Corrector(custom_confusion_path_or_dict='./my_custom_confusion.txt')
    # m.set_custom_word_freq(path=r'/Users/xuanchengwei/Desktop/git_clone/pycorrector/examples/kenlm/custom_word_freq.txt')
    # m.set_custom_confusion_path_or_dict('/Users/xuanchengwei/Desktop/git_clone/pycorrector/examples/kenlm/my_custom_confusion.txt')
    md_file = "/Users/xuanchengwei/my-data/core/H/extraordinary-fiction/娇妻美妾任君尝/霸王花魁传-娇妻美妾任君尝同人/霸王花魁传-娇妻美妾任君尝同人.md"
    lines = read_md_file(md_file)
    for l in lines:
        r = m.correct(l)
        errors = r['errors']
        errors = [t for t in errors if not isInNameList(r['source'],t[2])]
        if errors:
            print(errors)
            print_with_red_segments(r['source'], [(c, len(a)) for a, b, c in errors])
