from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tsr_functions import *
from sklearn.preprocessing import MultiLabelBinarizer



def get_relevant_words(X, y, nwords, featnames, tsr_function=information_gain_positive):
    nD,nF = X.shape
    positives = y.sum()
    negatives = nD - positives

    # computes the 4-cell contingency tables for each feature
    TP = np.asarray((X[y==1]>0).sum(axis=0)).flatten()
    FN = positives - TP
    FP = np.asarray((X[y==0]>0).sum(axis=0)).flatten()
    TN = negatives - FP
    _4cell = [ContTable(tp=TP[i], tn=TN[i], fp=FP[i], fn=FN[i]) for i in range(nF)]

    # applies the tsr_function to the 4-cell counters
    feat_informativeness = np.array(list(map(tsr_function, _4cell)))

    top_relevant_terms = np.argsort(-feat_informativeness)[:nwords]
    feat_names = np.asarray(featnames)[top_relevant_terms]
    feat_informativeness = feat_informativeness[top_relevant_terms]

    return list(zip(feat_names, feat_informativeness))


print('preparing corpus')
corpus = fetch_20newsgroups(subset='test', categories=['alt.atheism', 'comp.graphics', 'rec.motorcycles', 'sci.space', 'talk.politics.guns'])
documents = corpus.data
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5)
X = tfidf.fit_transform(documents)

# only if the dataset is single-label multiclass (i.e., if corpus.target has shape (ndocs,))
print('retrieving relevant terms')
mlb = MultiLabelBinarizer()
Y = mlb.fit_transform(corpus.target.reshape(-1, 1))
nC = Y.shape[1]
print(Y.shape)

nwords = 10
for i in range(nC):
    # getting the 10 most relevant terms for each class according to the (positive only) correlation to the
    # group label, as quantified by information gain
    class_i_relevant = get_relevant_words(X, Y[:,i], nwords, tfidf.get_feature_names())
    print(f'class {i}: ' + ', '.join([f'{word} ({rel:.3f})' for word, rel in class_i_relevant]))





