import os
import csv
from collections import Counter
import re


def get_cluster_text(cluster_dir):
    cluster_text = {}

    for file in os.listdir(cluster_dir):
        cluster_file = os.path.join(cluster_dir, file)
        cluster_name = os.path.basename(cluster_file)

        phrases = []
        with open(cluster_file, 'r') as file_reader:
            reader = csv.reader(file_reader, delimiter=' ')
            for row in reader:
                text = row[1].strip()
                phrases.append(text)

        cluster_text[cluster_name] = phrases

    return cluster_text


def clean_text(raw_text):
    removelist = '<=> '
    cleaned_text = re.sub(r'[^\w' + removelist + ']', '', raw_text)

    tokens = cleaned_text.lower().split()
    return tokens


def convert_to_frequency(tokens):
    counter = Counter()
    counter.update(tokens)

    freq_vector = {}
    for word, freq in counter.items():
        freq_vector[word] = freq

    return freq_vector
