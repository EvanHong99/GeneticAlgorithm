# -*- coding=utf-8 -*-
# @File     : BaseCrossover.py
# @Time     : 2022/10/9 14:08
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from typing import overload

class BaseCrossover(object):
    """
    0.8-1.0 is fine
    """

    def __init__(self, poc,proportion):
        """

        :param poc: probability of crossover
        :param proportion: proportion of crossover
        """
        self.poc = poc
        self.proportion=proportion

    @overload
    def crossover(self):
        pass