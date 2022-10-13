# -*- coding=utf-8 -*-
# @File     : ElitismSelection.py
# @Time     : 2022/10/9 10:29
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.operators.Selection.BaseSelection import BaseSelection
import numpy as np
from functools import reduce



class ElitismSelection(BaseSelection):
    """
    preserve portion p of the population as elites,
    and use them to replace the individuals with the lowest fitness in next generation
    """

    def __init__(self,pos):
        """

        :param p: portion of elites
        """
        self.pos=pos

    def select(self, fitness: np.ndarray)-> tuple[np.ndarray, np.ndarray]:
        """
        select elites
        Returns:
            good ones, bad ones
        """
        sort=fitness.argsort(kind="mergesort")[::-1]
        num=int(self.pos*len(fitness))
        return sort[:num],sort[len(fitness)-num:]




if __name__ == '__main__':
    es=ElitismSelection(0.5)
    print(es.select(np.array(range(100,200))))