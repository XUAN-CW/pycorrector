# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('../..')

from pycorrector import MacBertCorrector


def main():
    m = MacBertCorrector()
    error_sentences = [
        "里面藏了在他当时看来好多好多的钱和几个装着人参的玉盒",
        "感到蜜穴里的跳蛋不在跳动",
        "客官，妾身表演给你看好么"
    ]
    batch_res = m.correct_batch(error_sentences)
    for i in batch_res:
        print(i)
        print()

    # result:
    # {'source': '今天新情很好', 'target': '今天心情很好', 'errors': [('新', '心', 2)]}
    # {'source': '你找到你最喜欢的工作，我也很高心。', 'target': '你找到你最喜欢的工作，我也很高兴。', 'errors': [('心', '兴', 15)]}


if __name__ == "__main__":
    main()
