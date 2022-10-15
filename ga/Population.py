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
        self.origin_info=None
        self.pop_size = pop_size
        self.chrom_len = chrom_len
        self.info_path = info_path
        self.individuals = None
        self.encoding = chromo_representation

    def initialization(self):
        self.origin_info = pd.read_csv(self.info_path, sep='\s+', header=0)
        self.info=self.origin_info
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
        """
        add individuals while keep old ones
        Args:
            num:

        Returns:

        """
        individuals=self.individuals.tolist()
        new_individuals = []
        for i in range(num):
            a = np.arange(self.chrom_len + num, dtype=np.int8)
            np.random.shuffle(a)
            new_individuals.append(a.tolist())

        for i in range(self.pop_size):
            a = np.arange(self.chrom_len,self.chrom_len + num, dtype=np.int8)
            np.random.shuffle(a)
            individuals[i].extend(a.tolist())
        individuals.extend(new_individuals)

        self.pop_size += num
        self.chrom_len += num
        self.individuals=np.array(individuals)
        print(f"population updated {self.individuals.shape}")

    def update_info(self,env):
        "remember to update cost in class problem"
        x_shift=2*env*np.cos(np.pi*env/2)
        y_shift=2*env*np.sin(np.pi*env/2)
        self.info['XCOORD']= self.origin_info['XCOORD'] + x_shift
        self.info['YCOORD']= self.origin_info['YCOORD'] + y_shift
        print(f"update info at env {env}")

if __name__ == '__main__':
    pop = Population(10, 10, "../data/TSPTW_dataset.txt", Encoding.P)
    pop.initialization()
    # print(pop.individuals)
    pop.add_individuals(10)
    print(pop.individuals)
