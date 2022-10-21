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
from copy import deepcopy
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import defaultdict


class Population(object):
    """

    Store information about the population, calculations are in class Problem

    Attributes:
        individuals: np.ndarray. every individual is a route

    """

    def __init__(self, pop_size, chrom_len, info_path: str, chromo_representation: Encoding,is_clustered=False):
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
        self.origin_info = None
        self.pop_size = pop_size
        self.chrom_len = chrom_len
        self.info_path = info_path
        self.individuals = None
        self.encoding = chromo_representation
        self.is_clustered=is_clustered

    def init_info(self):
        self.origin_info = pd.read_csv(self.info_path, sep='\s+', header=0)
        self.info = self.origin_info


    def init_individuals(self, cluster: list[list] = None):
        """
        Notes:
            must update pop size and chromosome size before this func
        """

        def shuffle(cluster: list[list]):
            """
            two dimensional shuffle
            [[0,1,2,3],[4,5],[6,7,8]] -> [ [6, 7, 8],[2, 3, 0, 1], [4, 5]]
            """
            for i in range(len(cluster)):
                np.random.shuffle(cluster[i])
            np.random.shuffle(cluster)

        individuals = []
        if cluster is not None:
            for i in range(self.pop_size):
                shuffle(cluster)
                individuals.append(deepcopy(cluster))
            individuals = np.array(individuals, dtype=object)
        else:
            a = np.arange(self.chrom_len, dtype=np.int8)
            for i in range(self.pop_size):
                np.random.shuffle(a)
                individuals.append(deepcopy(a))
            individuals = np.array(individuals, dtype=np.int8)
        self.individuals=individuals

    def add_individuals(self, num):
        """
        add individuals while keep old ones
        Args:
            num:

        Returns:

        """
        individuals = self.individuals.tolist()
        new_individuals = []
        for i in range(num):
            a = np.arange(self.chrom_len + num, dtype=np.int8)
            np.random.shuffle(a)
            new_individuals.append(a.tolist())

        for i in range(self.pop_size):
            a = np.arange(self.chrom_len, self.chrom_len + num, dtype=np.int8)
            np.random.shuffle(a)
            individuals[i].extend(a.tolist())
        individuals.extend(new_individuals)

        self.pop_size += num
        self.chrom_len += num
        self.individuals = np.array(individuals)
        print(f"add_individuals {self.individuals.shape}")

    def update_info_env(self, env):
        "task2 remember to update cost in class problem"
        x_shift = 2 * env * np.cos(np.pi * env / 2)
        y_shift = 2 * env * np.sin(np.pi * env / 2)
        self.info['XCOORD'] = self.origin_info['XCOORD'] + x_shift
        self.info['YCOORD'] = self.origin_info['YCOORD'] + y_shift
        print(f"update info at env {env}")

    def init_shift_info(self, shift_distance):
        """
        create new individuals' info by shifting
        Args:
            shift_distance:

        Returns:

        """
        newpoints = deepcopy(self.info)
        newpoints['CUST_NO'] += self.pop_size
        newpoints['XCOORD'] += shift_distance
        self.info = pd.concat([self.info, newpoints], ignore_index=True)
        self.pop_size += self.pop_size
        self.chrom_len += self.pop_size
        # self.individuals = self.init_individuals(self.pop_size, self.chrom_len)

    def get_cluster(self, n_clusters, method="kmeans") -> list[list]:
        """

        Args:
            n_clusters:
            method:

        Returns:
            list of indexes of clustered genes
        """
        assert n_clusters <= 6
        if method == "kmeans":
            kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(self.info[["XCOORD", "YCOORD"]])
            # print(kmeans.labels_)
            clusters = []
            print(self.pop_size)
            for i in range(n_clusters):
                index = np.arange(self.pop_size, dtype=int)[kmeans.labels_ == i]
                clusters.append(list(index))
            return clusters
        else:
            raise NotImplementedError("method")

    @staticmethod
    def flatten_chromosome(clustered_chromo):
        res=[]
        for gene in clustered_chromo:
            res.extend(gene)
        return res



if __name__ == '__main__':
    pop = Population(100, 100, "../data/TSPTW_dataset.txt", Encoding.P)
    pop.init_info()
    pop.individuals= pop.init_individuals()
    print(pop.get_cluster(4))
