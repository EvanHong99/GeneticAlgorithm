# -*- coding=utf-8 -*-
# @File     : SwapMutation.py
# @Time     : 2022/10/8 19:43
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.operators.Mutation.BaseMutation import BaseMutation
from typing import overload
from bitarray import bitarray
import numpy as np
from Support import *


class SwapMutation(BaseMutation):

    def __init__(self,pom):
        """

        :param pom: probability of mutation
        """
        super().__init__()
        self.pom=pom

    def mutate(self,gene:np.ndarray,gType:ChromeRepr):
        """
        gType==ChromeRepr.P: randomly choose two gene and swap them
        :param gene:
        :param gType:
        :return:
        """
        assert gType==ChromeRepr.P
        if np.random.rand()<self.pom:
            pos1=int(len(gene)*np.random.rand())
            pos2=int(len(gene)*np.random.rand())
            temp=gene[pos1]
            gene[pos1]=gene[pos2]
            gene[pos2]=temp
        return gene



if __name__ == '__main__':
    gm=SwapMutation(1)
    a=np.array(range(100))
    print(gm.mutate(a,ChromeRepr.P))
    print(a)
