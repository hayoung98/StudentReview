import jieba
from gensim import corpora, models
import re
import csv
import matplotlib.pyplot as plt


def remove_punctuation(line):
    rule = re.compile(u"[^\u4e00-\u9fa5]")  # 只留下中文字
    line = rule.sub('',line)
    return line

with open('CS106_CS249_Student_Content(更新).csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    with open('stop_word_corex.txt') as file:
        All_sw = file.read()
        stop_word_list = All_sw.splitlines()

    words_list = []  # 分詞
    for row in rows:
        line = (row['Content'])
        line = remove_punctuation(line)
        words = [i for i in jieba.lcut(line, cut_all=False) if i not in stop_word_list]
        words_list.append(words)

    # print(seg_list)
    dictionary = corpora.Dictionary(words_list)
    # print(dictionary)
    corpus = [dictionary.doc2bow(words) for words in words_list]
    # print(corpus)
    perplexity_list = []
    x_label = []
    for topic_num in range(1,15):
        print("--------------------------------")
        lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=topic_num)
        perplexity_list.append(pow(2, lda.log_perplexity(corpus)))
        x_label.append(topic_num)
        for topic in lda.print_topics(num_words=10):
            docs = topic[1].split('+')
            print(topic[0]+1, docs)
    plt.plot(x_label,perplexity_list)
    plt.ylabel('perplexity')
    plt.xlabel('topic_num')
    plt.show()