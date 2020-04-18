Example for running one of the standard models (non-BYOB models)
python main.py 2 2 0.3 '/training_data/training-tweets.txt' '/test_data/test-tweets-given.txt'
In this case the program will use vocab 2, bigram classifier, and 0.3 delta.

Example for running the BYOB model
python main.py 2 4 0.3 '/training_data/training-tweets.txt' '/test_data/test-tweets-given.txt' 1
The delta value is ignored, n-gram size can be increased past 3, Optimal results were achieved for 4-gram (96% accuracy)

Code runs from the main.py file
