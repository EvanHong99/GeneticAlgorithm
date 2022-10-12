# -*- coding=utf-8 -*-
# @File     : Recombination.py
# @Time     : 2022/10/9 14:09
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.operators.Crossover.BaseCrossover import BaseCrossover
import numpy as np
from copy import deepcopy


class Recombination(BaseCrossover):
    def __init__(self, poc, proportion):
        """
        exchange half of the genes
        :param poc: probability of crossover
        """
        super().__init__(poc, proportion)

    def swap(self, chromo1, chromo2):
        """
        preserve part of chromo1 and change the rest to the order of which as in chromo2
        :param chromo1:
        :param chromo2:
        :return:
        """
        length = len(chromo1)
        child = deepcopy(chromo1)
        start = np.random.randint(length)
        end = start + int(length * (1-self.proportion))
        if end > length:
            swap_items = set(chromo1[end - length:start])
        else:
            swap_items = set(chromo1[:start])
            swap_items = swap_items.union(set(chromo1[end:]))

        sorted_items = []
        for c2 in chromo2:
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

    def crossover(self, chromo1: np.ndarray, chromo2: np.ndarray):

        assert len(chromo1) == len(chromo2)

        if np.random.rand() < self.poc:
            child1 = self.swap(chromo1, chromo2)
            child2 = self.swap(chromo2, chromo1)
            return child1, child2
        return chromo1, chromo2


if __name__ == '__main__':
    rec = Recombination(1,0.2)
    c1, c2 = rec.crossover(np.arange(0, 10, 1), np.arange(9, -1, -1))
    print(c1)
    print(c2)
