import numpy as np
import random
import bean
from matplotlib import pyplot as plt
import networkx as nx

ITERATION = 1000
TARGET = 0
EPSILON = 0.2 # a higher epsilon contributes to a lower segment
# PLOT_TIMESTEP = [0, 1, 2, 3, 4, 5, 10, 20, 50, 100]


class environment:
    def __init__(self, G):
        self.G = G

    def belief_revision(self):
        for user in self.G.nodes():
            xi = self.G.nodes[user]['belief'][TARGET]
            sum_xj = 0
            sum_j = 0
            for neighbour in self.G.successors(user):
                xj = self.G.nodes[neighbour]['belief'][TARGET]
                if abs(xi - xj) < EPSILON:
                    sum_xj += xj
                    sum_j += 1
            if sum_j > 0:
                xi = sum_xj / sum_j
            self.G.nodes[neighbour]['belief'][TARGET] = xi

    def simulation(self):
        for iteration in range(ITERATION):
            result = []
            for user in self.G.nodes():
                result.append(self.G.nodes[user]['belief'][TARGET])
            if iteration > 0:
                self.belief_revision()
            if iteration % 100 == 0:
                plot(result, iteration)

    def user_takes_action(self, user, time_step):
        pass



def plot(result, iteration):
    result.sort()
    plt.figure()
    plt.bar(range(len(result)), result)
    plt.title("Iteration step: " + str(iteration) + ' with ' + r'$\varepsilon=0.2$')
    plt.ylabel('Belief')
    plt.xlabel('Agent')
    # plt.show()
    # plt.savefig("result/random/" + str(iteration) + ".png")

    print("Iteration step: " + str(iteration))
    print(result)
    print('==================================')


if __name__ == "__main__":
    graph = bean.load_network("random")
    env = environment(graph)
    env.simulation()