import pandas as pd
from nltk.stem import WordNetLemmatizer
from gensim.models import KeyedVectors
import DAG

# nrc = pd.read_csv("../data/lexicon/NRC-Emotion-Lexicon-Wordlevel.txt", sep='\t', engine='python')
# nrc.columns = ["word", "sentiment", "value"]
# nrc = nrc[nrc['value'] == 1].drop(['value'], axis=1)
# nrc.reset_index(inplace=True, drop=True)
# nrc.to_csv("../data/processed/processed_nrc.csv")

# model = gensim.downloader.load('glove-wiki-gigaword-50')

# load the word2vec model
model = KeyedVectors.load('model.kv')

lemmatizer = WordNetLemmatizer()
wordgraph = DAG.DAG()
nrc = pd.read_csv('../data/processed/processed_nrc.csv', index_col=0)

# iterate over the words for each sentiment category, take the top5 most similar words to the current word
sentiments = ["positive", "negative", "anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]
for s in sentiments[2:3]:
    curr_sentiment = nrc[nrc['sentiment'] == s]['word'].tolist() # get current sentiment words
    words = filter(lambda x: x in model, curr_sentiment) # get words both in the model and curr_sentiment

    for w1 in words:
        top15 = model.most_similar(w1, topn=15)

        top5 = []
        for w2 in top15:
            # lemmatize so that there are no duplicates
            if lemmatizer.lemmatize(w2[0]) == w1:
                continue
            else:
                top5.append(w2)

            if len(top5) == 5:
                break

        for w2 in top5:
            wordgraph.add_edge(w1, w2[0], w2[1])
















