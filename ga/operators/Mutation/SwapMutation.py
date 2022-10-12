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
        super().__init__(pom)


    def mutate(self, chromo:np.ndarray):
        """
        gType==Encoding.P: randomly choose two chromo and swap them
        :param chromo:
        :return:
        """
        if np.random.rand()<self.pom:
            pos1=int(len(chromo) * np.random.rand())
            pos2=int(len(chromo) * np.random.rand())
            temp=chromo[pos1]
            chromo[pos1]=chromo[pos2]
            chromo[pos2]=temp
        return chromo



if __name__ == '__main__':
    gm=SwapMutation(1)
    a=np.array(range(100))
    print(gm.mutate(a))
    print(a)
