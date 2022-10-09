import numpy as np
import pandas as pd

topics = {}
topic_network = []
df = pd.read_csv('dataset/movies.csv', sep='::', header=None)
for i in range(len(df[2])):
    types = df[2][i].split('|')
    for n in range(len((types))):
        if topics.get(types[n]) is None:
            topics[types[n]] = 1
        else:
            value = topics[types[n]]
            value += 1
            topics[types[n]] = value
print(topics)
