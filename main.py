import sys

# remove first argument
sys.argv.pop(0)

# getting hyperparameters
VOCAB_TO_USE, N_GRAM_SIZE, DELTA, TRAINING_FILE, TESTING_FILE, *rest = sys.argv
