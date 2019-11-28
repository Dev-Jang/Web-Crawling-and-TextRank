# -*- coding: utf-8 -*-
from konlpy.tag import Kkma
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np

kkma = Kkma()
okt = Okt()
stopwords = ['중인' ,'만큼', '마찬가지', '꼬집었', "연합뉴스", "데일리", "동아일보", "중앙일보", "조선일보", "기자",
            "아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가",]
tfidf = TfidfVectorizer()
cnt_vec = CountVectorizer()
graph_sentence = []

def get_sentences():
    '''
    크롤링한 본문 내용 텍스트파일을 불러와
    Kkma.sentences()를 이용하여 문장단위로 나누어 준 후
    sentences를 return 한다.
    '''
    with open('crawl_result.txt', 'rt', encoding='utf8') as f:
        s = f.readlines()
        sentences = []
        for sentence in s:
            sentences.append(sentence[:-1])

    return sentences

def get_nouns(sentences):
    '''
    sentences를 받아 Okt.nouns()를 이용하여
    명사를 추출한 뒤 nouns를 return 한다.
    '''
    nouns = []
    for sentence in sentences:
        if sentence is not '':
            nouns.append(' '.join([noun for noun in okt.nouns(str(sentence)) if noun not in stopwords and len(noun) > 1]))

    return nouns

def build_sent_graph(sentence):
    '''
    명사로 이루어진 문장을 입력받아
    sklearn의 TfidfVectorizer.fit_transform을 이용하여
    tfidf matrix를 만든 후 Sentence graph를 return 한다.
    '''
    tfidf_mat = tfidf.fit_transform(sentence).toarray()
    graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
    return graph_sentence

def build_words_graph(sentence):
    '''
    명사로 이루어진 문장을 입력받아
    sklearn의 CountVectorizer.fit_transform을 이용하여
    matrix를 만든 후 word graph와 {idx: word}형태의 dictionary를 return 한다.
    '''
    cnt_vec_mat = normalize(cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
    vocab = cnt_vec.vocabulary_
    return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}

def get_ranks(graph, d=0.85):       # d = damping factor
    '''
    TextRank 알고리즘 식을 구현한 부분이며,
    {idx : rank 값} 형태의 dictionary를 return 한다.
    '''
    A = graph
    matrix_size = A.shape[0]
    for id in range(matrix_size):
        A[id, id] = 0               # diagonal 부분을 0으로
        link_sum = np.sum(A[:,id])  # A[:, id] = A[:][id]
        if link_sum != 0:
            A[:, id] /= link_sum
        A[:, id] *= -d
        A[id, id] = 1

    B = (1-d) * np.ones((matrix_size, 1))
    ranks = np.linalg.solve(A, B)   # 연립방정식 Ax = b
    return {idx: r[0] for idx, r in enumerate(ranks)}

def summarize(sent_num=3):
    summary = []
    index=[]
    for idx in sorted_sent_rank_idx[:sent_num]:
        index.append(idx)

    index.sort()
    for idx in index:
        summary.append(sentences[idx])

    return summary

def keywords(word_num=30):
    rank_idx = get_ranks(words_graph)
    sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)
    
    keywords = []
    index=[]
    for idx in sorted_rank_idx[:word_num]:
        index.append(idx)

    #index.sort()
    for idx in index:
        keywords.append(idx2word[idx])

    return keywords

def main():
    sentences = get_sentences()
    nouns = get_nouns(sentences)

    sent_graph = build_sent_graph(nouns)
    words_graph, idx2word = build_words_graph(nouns)

    sent_rank_idx = get_ranks(sent_graph)
    sorted_sent_rank_idx = sorted(sent_rank_idx, key=lambda k: sent_rank_idx[k], reverse=True)

    word_rank_idx = get_ranks(words_graph)
    sorted_word_rank_idx = sorted(word_rank_idx, key=lambda k: word_rank_idx[k], reverse=True)

    for row in summarize(3):
        print(row)
    print('keywords :', keywords())

main()