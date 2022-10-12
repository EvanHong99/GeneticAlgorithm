# -*- coding=utf-8 -*-
# @File     : Population.py
# @Time     : 2022/10/4 17:23
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

import numpy as np
import pandas as pd
from Support import Encoding


class Population(object):
    """

    Store information about the population, calculations are in class Problem

    Attributes:
        individuals: np.ndarray. every individual is a route

    """

    def __init__(self, pop_size, chrom_len, info_path: str, chromo_representation: Encoding):
        """

        :param pop_size:
        :param chrom_len:
        :param info_path: 每个客户的具体信息，比如位置等
                    '''
                         XCOORD  YCOORD  DEMAND  READY_TIME  DUE_TIME  SERVICE_TIME
        CUST_NO
        1          29.0    24.0     0.0         0.0     862.0           0.0
        2           1.0    28.0     0.0       273.0     289.0           0.0
        3          25.0    19.0     0.0         2.0      61.0           0.0
        '''
        :param chromo_representation:

        """
        self.info = None
        self.pop_size = pop_size
        self.chrom_len = chrom_len
        self.info_path = info_path
        self.individuals = None
        self.encoding = chromo_representation

    def initialization(self):
        self.info = pd.read_csv(self.info_path, sep='\s+', header=0)
        self.individuals = self._init_individuals_(self.pop_size, self.chrom_len)

    def _init_individuals_(self, pop_size, chrom_len) -> np.ndarray:
        """
        every individual is a route
        :param pop_size:
        :param chrom_len:
        :return:
        """
        individuals = []
        for i in range(pop_size):
            a = np.arange(chrom_len, dtype=np.int8)
            np.random.shuffle(a)
            individuals.append(a)
        individuals = np.array(individuals, dtype=np.int8)
        return individuals

    def add_individuals(self, num):
        self.pop_size += num
        self.chrom_len += num


#         todo 注意避免重复


if __name__ == '__main__':
    pop = Population(100, 100, "../data/TSPTW_dataset.txt", Encoding.P)
    print(pop.individuals)
    print(pop.info)
