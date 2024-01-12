# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import sys

sys.path.append("../..")
from pycorrector import GptCorrector

if __name__ == '__main__':
    error_sentences = [
        "里面藏了在他当时看来好多好多的钱和几个装着人参的玉盒",
        "感到蜜穴里的跳蛋不在跳动",
        "客官，妾身表演给你看好么"
    ]
    m = GptCorrector()

    batch_res = m.correct_batch(error_sentences)
    for i in batch_res:
        print(i)
        print()
