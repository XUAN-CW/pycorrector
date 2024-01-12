# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append("../..")
from pycorrector import MacBertCorrector
from pycorrector import ConfusionCorrector

if __name__ == '__main__':
    error_sentences = [
        '其实，最征服阳大根的，是那销魂蚀骨的眼神',  # 漏召回
    ]

    model1 = MacBertCorrector()
    # add confusion corrector for post process
    confusion_dict = {"杨大根": "阳大根"}
    model2 = ConfusionCorrector(custom_confusion_path_or_dict=confusion_dict)
    for line in error_sentences:
        r1 = model1.correct(line)
        correct_sent = r1['target']
        # print("query:{} => {} err:{}".format(line, correct_sent, r1['errors']))
        r2 = model2.correct(correct_sent)
        corrected_sent2 = r2['target']
        if corrected_sent2 != correct_sent:
            print("update, query:{} => {} err:{}".format(correct_sent, corrected_sent2, r2['errors']))
