# -*- coding=utf-8 -*-
# @File     : Population.py
# @Time     : 2022/10/4 17:23
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

import numpy as np
import pandas as pd
from Support import ChromeRepr


class Population(object):
    """
    todo :种群不断有新人加进来
    Population : class - 种群类
    Attributes:
        individuals: np.matrix. every individual is a route

    """
    def __init__(self, pop_size, chrom_len, info_path:str,chromo_representation:ChromeRepr):
        """

        :param pop_size:
        :param chrom_len:
        :param info: 每个客户的具体信息，比如位置等
        """
        self.pop_size = pop_size
        self.chrom_len = chrom_len
        # self.info=pd.read_csv(info_path,sep='\s+',header=0,index_col=0)
        self.cost=dict(dict(list))
        self.individuals=None
        self.chrome_repr=chromo_representation

    def _init_individuals_(self,pop_size,chrom_len)->np.matrix:
        """
        every individual is a route
        :param pop_size:
        :param chrom_len:
        :return:
        """
        individuals = []
        for i in range(pop_size):
            a=np.arange(1,chrom_len+1,1,dtype=np.int8)
            np.random.shuffle(a)
            individuals.append(a)
        individuals=np.matrix(individuals,dtype=np.int8)
        return individuals

    def calc_fitness(self,chromesome):
        temp=chromesome.append(chromesome[0])
        fitness=0
        for i in range(len(temp)-1):
            fitness+=self.cost[chromesome[i]][chromesome[i+1]]
        return fitness



if __name__ == '__main__':
    # pop=Population(10,10,"../data/TSPTW_dataset.txt",ChromeRepr.P)
    # print(pop.individuals)
    cost = dict(dict(list))
    cost[1][2]=[3,4]
    print(cost[1][2])
