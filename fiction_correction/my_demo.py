# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys

sys.path.append(".")
from pycorrector import Corrector


def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    return lines


if __name__ == '__main__':
    # m = Corrector(proper_name_path='./my_custom_proper.txt')

    m = Corrector(custom_confusion_path_or_dict='./my_custom_confusion.txt')

    error_sentences = [
        "里面藏了在他当时看来好多好多的钱和几个装着人参的玉盒",
        "感到蜜穴里的跳蛋不在跳动",
        "客官，妾身表演给你看好么"
    ]
    for l in error_sentences:
        r = m.correct(l)
        if r['errors']:
            print(r)