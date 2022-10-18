# -*- coding=utf-8 -*-
# @File     : ClusterSwapMutation.py
# @Time     : 2022/10/17 12:33
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:
from ga.operators.Mutation.BaseMutation import BaseMutation
import numpy as np
from copy import deepcopy


class ClusterSwapMutation(BaseMutation):
    def __init__(self, pom, pocm):
        super(ClusterSwapMutation, self).__init__(pom)
        self.pocm = pocm

    def __mutate_gene__(self,gene):
        pos1=int(len(gene) * np.random.rand())
        pos2=int(len(gene) * np.random.rand())
        temp=deepcopy(gene[pos1])
        gene[pos1]=gene[pos2]
        gene[pos2]=temp
        return gene

    def mutate(self, chromo: np.ndarray, cluster_num):
        "swap two gene segments"
        if np.random.rand() < self.pocm:
            # swap cluster order
            pos1 = int(len(chromo) * np.random.rand())
            pos2 = int(len(chromo) * np.random.rand())
            temp = deepcopy(chromo[pos1])
            chromo[pos1] = chromo[pos2]
            chromo[pos2] = temp

        # mutate one gene
        if np.random.rand() < self.pom:
            which_cluster=np.random.randint(len(chromo))
            chromo[which_cluster]=self.__mutate_gene__(chromo[which_cluster])

        return chromo
