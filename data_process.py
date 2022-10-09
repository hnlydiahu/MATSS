import numpy as np
import pandas as pd


df = pd.read_csv('dataset/movies.csv', sep='::', header=None)
for i in range(len(df[2])):
    print(df[2][i])
