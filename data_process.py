import numpy as np
import pandas as pd
import networkx as nx
import pickle
import math
from matplotlib import pyplot as plt


def create_topic_network():
    topics = {}
    topic_network = []
    topic_arr = []

    df = pd.read_csv('dataset/movies.csv', sep='::', header=None)
    # get N^a
    for i in range(len(df[2])):
        types = df[2][i].split('|')
        for n in range(len((types))):
            if topics.get(types[n]) is None:
                topics[types[n]] = 1
            else:
                value = topics[types[n]]
                value += 1
                topics[types[n]] = value

    # get N^a,b
    # initialize topic network

    # temp = topics
    # for t in temp:
    #     temp[t] = 0
    # for t in topics:
    #     topic_network[t] = temp
    topic_arr = list(topics.keys())
    print(topic_arr)
    topic_network = [[0 for x in range(len(topic_arr))] for y in range(len(topic_arr))]

    for i in range(len(df[2])):
        types = df[2][i].split('|')
        # calculate topic correlation
        if len(types) > 1:
            for t in range(len(types)):
                current_temp = []
                for temp in range(len(types)):
                    if temp != t:
                        current_temp.append(types[temp])
                a = types[t]
                for b in current_temp:
                    correlation = topic_network[topic_arr.index(a)][topic_arr.index(b)]
                    new_correlation = correlation + 1
                    topic_network[topic_arr.index(a)][topic_arr.index(b)] = new_correlation
    print(topic_network)

    # create network by nx
    G = nx.Graph()
    G.add_nodes_from(topic_arr)
    node_dic = {}
    edge_dic = {}

    for t in G.nodes():
        node_dic[t] = {
            'topicID': list(topics.keys()).index(t),
            'number': topics.get(t),
            'H': - (topics.get(t) / sum(list(topics.values()))) * math.log(topics.get(t) / sum(list(topics.values())))
        }
    nx.set_node_attributes(G, node_dic)

    for a in topic_network:
        for b in a:
            if a.index(b) != topic_network.index(a) and b != 0:
                Hab = - (b / sum(list(topics.values()))) * math.log(b / sum(list(topics.values())))
                calculate_dependence_degree(G, topic_arr[topic_network.index(a)], topic_arr[a.index(b)], Hab)

    pickle.dump(G, open('./dataset/topic_network.G', 'wb'))


def calculate_dependence_degree(G, a, b, Hab):
    Ha = G.nodes()[a]['H']
    Hb = G.nodes()[b]['H']
    dab = Ha + Hb - Hab
    G.add_edge(a, b)
    G[a][b]['dependence'] = dab

def load_network(dataset):
    path = './dataset/' + dataset + '.G'
    G = pickle.load(open(path, 'rb'))
    print(nx.info(G))

    return G

if __name__ == "__main__":
    # create_topic_network()
    G = load_network('topic_network')
    # pos = nx.spiral_layout(G)
    weights = [w * 3 for w in nx.get_edge_attributes(G, 'dependence').values()]
    node_size = nx.get_node_attributes(G, 'number').values()
    nx.draw(G, width=list(weights), with_labels=True, font_size=8, node_size=list(node_size), node_color='#ADD8E6')

    plt.savefig('result/topic_network.pdf')
    plt.show()

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
