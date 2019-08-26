import gensim.models as g
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

'''
PARAM str
    headline
RETURN list (300-dim)
    [-0.33011487 -0.0801257   0.13328408  0.3723667   0.39516467  0.6148282
     -0.12310064  0.06089959  0.06378347 -0.5073989   0.10822874  ...        ]
'''
def get_headline_vector(headline):
    # parameters
    model = "data/apnews_dbow/doc2vec.bin"
    start_alpha = 0.01
    infer_epoch = 1000

    # load model
    m = g.Doc2Vec.load(model)

    # infer test vectors
    doc = headline.split()
    vec = m.infer_vector(doc, alpha=start_alpha, steps=infer_epoch)
    return vec

'''
PARAM list
    headlines (n entries)
RETURN array (n x n)
    [[1.0000002 0.9999873]
    [0.9999873 1.0000006]]
'''
def get_headline_similarity(headlines):
    vectors = [get_headline_vector(headline) for headline in headlines]
    return cosine_similarity(vectors)

if __name__ == '__main__':
    df = pd.read_csv('text.csv')
    headlines = df['title'].to_list()
    vectors = np.array([get_headline_vector(headline) for headline in headlines])
    df = pd.DataFrame(vectors)
    df['headline'] = headlines
    df.columns = [_ for _ in range(300)] + ['headline']
    df.to_csv('data/news_vectors.csv', index=False)

