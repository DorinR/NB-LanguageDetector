import sys
from model import Model
from read_in_tweets import read_tweets_from
from tweet import Tweet

# remove first argument
sys.argv.pop(0)

# getting hyperparameters
VOCAB_TO_USE, N_GRAM_SIZE, DELTA, TRAINING_FILE, TESTING_FILE, *rest = sys.argv

# create model object that stores all out hyperparameters
model = Model(VOCAB_TO_USE, N_GRAM_SIZE, DELTA, TRAINING_FILE, TESTING_FILE)

# read in training_data
training_tweets = read_tweets_from(TRAINING_FILE)

# read in testing_data
testing_tweets = read_tweets_from(TESTING_FILE)
