# code for reading-in data from txt file re-used from Project 1
import sys
from tweet import Tweet
from typing import List


def read_tweets_from(filename: str) -> List[Tweet]:
    # get the path to the current directory
    current_directory = sys.path[0]

    # construct the absolute path to the file containing the puzzle data
    full_filename = current_directory + filename

    # read-in data file
    with open(full_filename, 'r') as f:
        data_with_whitespaces = f.readlines()

    # remove newline characters
    data = []
    for line in data_with_whitespaces:
        data.append(line.strip())

    tweets = []
    for i in range(len(data)):
        # print(i+1)
        try:
            id_, user, lang, *text = data[i].split()
            tweets.append(Tweet(id_, user, lang, ' '.join(text)))
        except:
            print(
                f'Error parsing line {i+1} of file {filename}. This line was skipped')

    return tweets
