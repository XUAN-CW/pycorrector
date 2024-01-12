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
        "其实，最征服阳大根的，是那销魂蚀骨的眼神",
        "感到蜜穴里的跳蛋不在跳动",
        "客官，妾身表演给你看好么"
    ]
    m = GptCorrector()

    batch_res = m.correct_batch(error_sentences)
    for i in batch_res:
        print(i)
        print()
