# -*- coding=utf-8 -*-
# @File     : ClusterRecombination.py
# @Time     : 2022/10/9 14:09
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.operators.Crossover.BaseCrossover import BaseCrossover
import numpy as np
from copy import deepcopy


class ClusterRecombination(BaseCrossover):
    def __init__(self, poc, proportion, pocc):
        """
        exchange 1 of the genes
        :param poc: probability of clustered crossover
        """
        super(ClusterRecombination, self).__init__(poc, proportion)
        self.pocc = pocc

    def map_cluster(self, chromo1, chromo2):
        """

        Args:
            chromo1:
            chromo2:

        Returns:
            the index in chromo2 of every gene in chromo1
        """
        mapper = {}
        table = np.zeros(len(chromo1))
        for i in range(len(chromo1)):
            gene1 = set(chromo1[i])
            for j in range(len(chromo2)):
                if table[j] == 0 and set(chromo2[j]) == gene1:
                    table[j] = 1
                    mapper[i] = j
                    break
        return mapper

    def __swap__(self, chromo1, chromo2):
        """
        swap half segments of genes, produce one child
        todo fix the swap between [[0],[1],[2],[3]] [[3],[0],[1],[2]] on [[2],[3]], because they are the same path
        """
        mapper = self.map_cluster(chromo1, chromo2)  # note it is the mapper for chromo2
        # print(mapper)
        length = len(chromo1)  # with CP Encoding
        child = deepcopy(chromo1)
        # np.random.seed(0)
        start = np.random.randint(length)  # [start, start+int(length/2)] preserved segment
        end = start + int(length / 2)
        temp = list(range(length))
        if end > length:
            swap_index1 = temp[end - length:start]
        else:
            swap_index1 = temp[end:]
            swap_index1.extend(temp[:start])
        # print("swap_index1",swap_index1)

        #     swap
        index2 = []
        for si in swap_index1:
            index2.append(mapper[si])
        index2 = sorted(index2)
        # print(index2)
        for i1 in range(len(swap_index1)):
            child[swap_index1[i1]] = chromo2[index2[i1]]
        return child

    def __swap_gene__(self, gene1, gene2):
        length = len(gene1)
        child = deepcopy(gene1)
        start = np.random.randint(length)
        end = start + int(length * (1 - self.proportion))
        if end > length:
            swap_items = set(gene1[end - length:start])
        else:
            swap_items = set(gene1[:start])
            swap_items = swap_items.union(set(gene1[end:]))

        sorted_items = []
        for c2 in gene2:
            if c2 in swap_items:
                sorted_items.append(c2)
                swap_items.remove(c2)

        #     swap
        if end > length:
            child[end - length:start] = sorted_items
        else:
            split = length - end
            # print(start,end, split, sorted_items[:split], sorted_items[split:])
            child[end:] = sorted_items[:split]
            child[:start] = sorted_items[split:]
        return child

    def crossover(self, chromo1: np.ndarray, chromo2: np.ndarray, cluster_num):

        assert len(chromo1) == len(chromo2)
        if np.random.rand() < self.pocc:
            child1 = self.__swap__(chromo1, chromo2)
            child2 = self.__swap__(chromo2, chromo1)
            chromo1, chromo2 = child1, child2

        if np.random.rand() < self.poc:
            child1, child2 = deepcopy(chromo1), deepcopy(chromo2)
            mapper = self.map_cluster(chromo1, chromo2)
            which_cluster = np.random.randint(len(chromo1))
            child1[which_cluster] = self.__swap_gene__(chromo1[which_cluster], chromo2[mapper[which_cluster]])

            mapper = self.map_cluster(chromo2, chromo1)
            which_cluster = np.random.randint(len(chromo2))
            child2[which_cluster] = self.__swap_gene__(chromo2[which_cluster], chromo1[mapper[which_cluster]])
            chromo1, chromo2 = child1, child2

        return chromo1, chromo2


if __name__ == '__main__':
    def shuffle(cluster: list[list]):
        for i in range(len(cluster)):
            np.random.shuffle(cluster[i])
        np.random.shuffle(cluster)


    rec = ClusterRecombination(0.5,0.5,1)
    # cluster = [[0, 1, 2, 3], [4, 5], [6, 7, 8], [9]]
    # cluster1 = [[5, 4], [8, 7, 6], [1, 0, 2, 3], [9]]
    cluster = [list(range(100)), list(range(100,200))]
    cluster1 = [list(range(100)), list(range(100,200))]
    individuals = []
    shuffle(cluster)
    # print(cluster)
    shuffle(cluster1)
    individuals.append(cluster)
    individuals.append(cluster1)
    print(individuals)
    individuals = np.array(individuals, dtype=object)
    for i in range(100):
        individuals[0], individuals[1] = rec.crossover(individuals[0], individuals[1],len(cluster))
    # print(c1)
    # print(c2)
    print(individuals)
