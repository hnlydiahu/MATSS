import networkx as nx
import numpy as np
import random
import pickle

TOPIC = 10

def generate_network(file_path):
    G = nx.gnm_random_graph(10, 30, directed=True)
    print(nx.info(G))

    node_dic = {}
    # edge_dic = {}

    for u in G.nodes():
        node_dic[u] = {
            # 'belief': np.ones(TOPIC)/TOPIC
            'belief': np.random.rand(TOPIC)
        }

    nx.set_node_attributes(G, node_dic)
    pickle.dump(G, open('./dataset/' + file_path + '_' + str(TOPIC) + '.G', 'wb'))
    pickle.dump(node_dic, open('./dataset/' + file_path + '_' + str(TOPIC) + '.node', 'wb'))
    # pickle.dump(edge_dic, open('./dataset/' + file_path + '_' + str(TOPIC) + '.edge', 'wb'))


def load_network(dataset):
    path = './dataset/' + dataset + '_' + str(TOPIC) + '.G'
    G = pickle.load(open(path, 'rb'))
    print(nx.info(G))

    return G


if __name__ == "__main__":
    load_network("random")