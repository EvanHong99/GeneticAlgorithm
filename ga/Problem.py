# -*- coding=utf-8 -*-
# @File     : Problem.py
# @Time     : 2022/10/4 17:25
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description: 问题类是用来存储与待求解问题相关信息的一个类。

import os
from typing import overload
import numpy as np
import pandas as pd


class Problem:
    def __init__(self):
        """
        存放目标函数的参数
        """
        self.cost=None


    @overload
    def init_cost(self, info:pd.DataFrame):
        """
        init the cost between two customer
        Args:
            info:

        Returns:

        """
        pass

    @overload
    def calc_fitness(self, chromosome):
        """
        Individual level. Fitness evaluates the chance that an individual is selected to produce children.
        It should be implemented in problem, because different problems will have different fitness funcs
        :param chromosome:
        :return:
        """
        pass

    def calc_distance(self, chromosome):
        temp = np.append(chromosome,chromosome[0])
        distance = 0
        for i in range(len(temp) - 1):
            distance += self.cost[temp[i]][temp[i + 1]]
        return distance

    @overload
    def fitness_preimage(self):
        """
        preimage of fitness
        Returns:

        """
        pass

    @overload
    def objective_func(self):
        """
        calculate the overall score about the population
        :return:
        """
        pass
