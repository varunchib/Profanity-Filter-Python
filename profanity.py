import os
import sys
import string
import re
import numpy as np
import pandas as pd
import profanity_check

# Define a function to clean up the text by removing punctuation and extra whitespace
def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

# Define a function to score the level of profanity in a sentence
def profanity_score(sentence):
    return np.mean(profanity_check.predict([sentence]))

# Define the main function that reads in a file and processes each sentence
def main(filename):
    with open(filename, 'r') as f:
        sentences = f.read().split('.')
    sentences = [clean_text(s) for s in sentences]
    scores = [profanity_score(s) for s in sentences]
    df = pd.DataFrame({'Sentence': sentences, 'Profanity Score': scores})
    print(df)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python profanity.py filename')
    else:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('File not found')
        else:
            main(filename)
