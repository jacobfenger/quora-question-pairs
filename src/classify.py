import csv
import re
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from matplotlib import pyplot as plt


TRAIN_FILE = '../data/train.csv'
TEST_FILE = '../data/test.csv'

# Generalize the text by removing punctuation, expanding contractions,
# and making everything lowercase
def process_text(text):
    # Make text lowercase
    text = text.lower()

    # Remove punctation or grammer, it just gets in the way during the training
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    return text

def read_data():

    train_data = {'text1': [], 'text2': [], 'labels': []}
    test_data = {'text1': [], 'text2': []}

    # Read train data
    with open(TRAIN_FILE, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader) # Skip header information
        for row in reader:
            text1 = process_text(row[3])
            train_data['text1'].append(text1)
            text2 = process_text(row[4])
            train_data['text2'].append(text2)
            train_data['labels'].append(int(row[5]))

    # Read test data
    with open(TEST_FILE, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            text1 = process_text(row[1])
            test_data['text1'].append(text1)
            text2 = process_text(row[2])
            test_data['text2'].append(text2)

    return train_data, test_data

def vectorize(train_data, test_data):

    print train_qs

def main():
    train, test = read_data()
    vectorize(train, test)



if __name__ == '__main__':
    main()
