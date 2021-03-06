import csv, re, jieba, monpa
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from corextopic import corextopic as ct
import _pickle as cPickle
from datetime import datetime
import sys
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%m-%d_%H_%M")
print("date and time =", dt_string)
print('Argument List:', str(sys.argv))
'''參數1:分幾類  參數2:source data  參數3:1.重新斷詞or2.讀斷詞檔'''
N_topic = int(sys.argv[1])
source_file = sys.argv[2]
Case = sys.argv[3]


def remove_punctuation(line):
    # rule = re.compile(u"[^\u4e00-\u9fa5, \u0041-\u005a, \u0060-\u007a]")  # 留下中文和英文
    rule = re.compile(u"[^\u4e00-\u9fa5]")  # 留下中文
    line = rule.sub('', line)
    return line


def cut(rows, stop_word_list, case):
    words_list = []  # ex. ['你','我','他'....]
    Label = []  # ex. ['A',...'B',...'C',...]
    for row in rows:
        line = (row['Content'])
        line = remove_punctuation(line)
        if case == '1':
            words = [
                i for i in jieba.lcut(line, cut_all=False)
                if i not in stop_word_list
            ]
        elif case == '2':
            words = [i for i in monpa.cut(line) if i not in stop_word_list]
        words[:] = ['，'.join(words[:])]
        words_list.append(words[0])
        label = (row['Label'])
        Label.append(label)
    return words_list, Label


def get_anchor():
    with open('anchor.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f:
            a.append(line.split())
        return a


if __name__ == '__main__':
    with open(source_file) as csvfile:
        rows = csv.DictReader(csvfile)
        with open('stop_word_corex.txt',encoding='utf-8') as file:
            All_sw = file.read()
            stop_word_list = All_sw.splitlines()
        if Case == '1':
            cut_case = input('1.jieba or 2.monpa')
            words_list, Label = cut(rows, stop_word_list, cut_case)
            cPickle.dump(words_list,
                         open('words_list_' + cut_case + '.pkl', 'wb'))
        elif Case == '2':
            words_list = cPickle.load(open('words_list_2.pkl', 'rb'))

        anchor = get_anchor()

        for j in range(100):
            vectorizer = CountVectorizer(
                token_pattern='\\b\\w+\\b')  # 原本只使用2個字以上的詞，改為1個字即可使用
            X = vectorizer.fit_transform(words_list)
            words = list(np.asarray(vectorizer.get_feature_names()))
            topic_model = ct.Corex(n_hidden=N_topic, words=words, seed=3)
            # topic_model = cPickle.load(open('model_monpa.pkl', 'rb'))

            if j > 0:
                for j in range(N_topic):
                    anchor_words = input(
                        'input topic_%s\'s anchor words(split with space):\n' %
                        str(j + 1))
                    t = anchor_words.split()
                    for word in t:
                        anchor[j].append(word)
                    print('本次新增anchor', t)
            print(anchor)
            topic_model.fit(X, words=words, anchors=anchor,
                            anchor_strength=4)  # anchors目前是自己設定
            # cPickle.dump(topic_model, open('model.pkl', 'wb'))

            topics = topic_model.get_topics(n_words=20)
            for n, topic in enumerate(topics):
                words, _ = zip(*topic)
                topic_str = str(n + 1) + ': ' + ','.join(words)
                print(topic_str)

            df1 = pd.DataFrame(topic_model.p_y_given_x)
            df1.to_csv('.\\report\\report' + dt_string + '.csv', index=True)
