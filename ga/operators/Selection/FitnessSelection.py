# -*- coding=utf-8 -*-
# @File     : FitnessSelection.py
# @Time     : 2022/10/13 21:35
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.operators.Selection.BaseSelection import BaseSelection
import numpy as np

class FitnessSelection(BaseSelection):
    def __init__(self):
        pass

    def select(self,fitness:np.ndarray):
        """

        Args:
            fitness:

        Returns:
            the indexes of individuals to produce children
        """
        def get_intervals(fitness):
            "construct ascending list, which is the probability of each individual being selected"
            intervals = np.empty_like(fitness)
            s = 0
            for i in range(len(fitness)):
                s += fitness[i]
                intervals[i] = s
            return intervals

        def find_idx(left, right, val, intervals):
            "which one is selected"
            if left == right:
                return left
            mid = int((left + right) / 2)
            if val <= intervals[mid]:
                return find_idx(left, mid, val, intervals)
            else:
                return find_idx(mid + 1, right, val, intervals)

        total=sum(fitness)
        intervals=get_intervals(fitness)

        selected=np.empty_like(fitness)
        for i in range(len(fitness)):
            selected[i]=find_idx(0,len(fitness)-1,total*np.random.rand(),intervals)

        return selected.astype(int)



if __name__ == '__main__':
    es=FitnessSelection()
    print(es.select(np.array(range(100))))