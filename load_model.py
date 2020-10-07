import pandas as pd
import _pickle as cPickle

if __name__ == '__main__':
    topic_model = cPickle.load(open('model_monpa.pkl', 'rb'))

    topics = topic_model.get_topics(n_words=20)

    for n, topic in enumerate(topics):
        words, _ = zip(*topic)
        topic_str = str(n + 1) + ': ' + ','.join(words)
        print(topic_str)

    df1 = pd.DataFrame(topic_model.p_y_given_x)
    df1.to_csv('report1.csv', index=True)
