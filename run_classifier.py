from model import Model
from tweet import Tweet
from typing import List, Dict
from classifiers.unigram_classifier import UnigramClassifier
from classifiers.bigram_classifier import BigramClassifier
from classifiers.trigram_classifier import TrigramClassifier


def run_classifier(model: Model, training_tweets: List[Tweet], testing_tweets: List[Tweet]):

    # instantiate classifier
    if model.n_gram_size == 1:
        classifier = UnigramClassifier(model, training_tweets, testing_tweets)
    elif model.n_gram_size == 2:
        classifier = BigramClassifier(model, training_tweets, testing_tweets)
    else:
        classifier = TrigramClassifier(model, training_tweets, testing_tweets)

    # train model
    classifier.train()

    # classify test tweets
    classifier.classify()

    # compute evaluation stats
    classifier.evaluate()

    # write trace and eval to .txt files
    classifier.save()
