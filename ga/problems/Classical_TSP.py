# -*- coding=utf-8 -*-
# @File     : Classical_TSP.py
# @Time     : 2022/10/8 22:24
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.Problem import Problem
import pandas as pd
import numpy as np


class Classical_TSP(Problem):
    def __init__(self, maxpop=100, max_chromo_len=100):
        super().__init__(maxpop, max_chromo_len)

    def _get_cost_(self, info1, info2):
        """
        Euclidean Distance
        :param info1:
        :param info2:
        :return:
        """
        return np.sqrt((info1['XCOORD'] - info2['XCOORD'])**2 + (info1['YCOORD'] - info2['YCOORD'])**2)

    def init_cost(self, info: pd.DataFrame):
        for i in range(info.shape[0]):
            for j in range(info.shape[0]):
                if i == j: continue
                self.cost[i][j] = self._get_cost_(info.iloc[i], info.iloc[j])

    def objective_func(self, all_fitness):
        return sum(all_fitness) / len(all_fitness)

    def calc_fitness(self, chromosome):
        """
        calculate the fitness of one chromosome
        :param chromosome:
        :return:
        """

        temp = np.append(chromosome,chromosome[0])
        fitness = 0
        for i in range(len(temp) - 1):
            fitness += self.cost[temp[i]][temp[i + 1]]
        return 1000/fitness

    def fitness_preimage(self, fitness):
        return 1000/fitness