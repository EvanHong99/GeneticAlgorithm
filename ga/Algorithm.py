# -*- coding=utf-8 -*-
# @File     : Algorithm.py
# @Time     : 2022/10/4 17:23
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description: 算法设置类是用来存储与算法运行参数设置相关信息的一个类。
'''
算法流程
Step1：对解空间进行编码；
Step2：随机产生包含n个个体的初始群体；
Step3：适应度评估检测个体适应度；
Step4：while< 为满足迭代终止条件>；
Step5：利用选择算子选择出若干个体进入交配池；
Step6：随机选择交配池中的两个个体，按照交叉概率进行交叉操
作；
Step7：变异算子通过按变异概率随机反转某些（个） 基因位；
Step8：适应度评估检测个体适应度；
Step9：end
'''

from typing import overload,Union
from Population import Population
from Problem import Problem
import matplotlib.pyplot as plt
from problems.Classical_TSP import Classical_TSP
from Support import Encoding


class Algorithm(object):
    """
    Algorithm : class - 算法类的顶级父类
    描述:
        算法设置类是用来存储与算法运行参数设置相关信息的一个类。
    属性:
        name            : str      - 算法名称（可以自由设置名称）。

        problem         : class <Problem> - 问题类的对象。
        population      : class <Population> - 种群对象。

        MAXGEN          : int      - 最大进化代数。
"""
    def __init__(self, problem, population, MAXGEN,pos,poc,proportion,pom):
        self.MAXGEN = MAXGEN
        self.population = population
        self.problem = problem
        self.history=[]
        self.ope_sel=None
        self.ope_cro=None
        self.ope_mut=None
    @overload
    def run(self):
        pass

    def draw(self,routine):

        # 各个点的经纬度及编号
        l=self.population.info.loc[routine,["XCOORD","YCOORD","CUST_NO"]].values

        def drawPic(dots):
            plt.figure(figsize=(10, 6))
            plt.xlabel('x', fontproperties="simhei")  # x轴的标题
            plt.ylabel('y', fontproperties="simhei")  # y轴的标题
            # 绘制各个点及点所代表地点名称
            for i in range(len(dots) - 1):
                plt.text(l[i][0], l[i][1], str(l[i][2]), color='#0085c3', fontproperties="simhei")
                plt.plot(l[i][0], l[i][1], 'o', color='#0085c3')
            # 连接各个点
            for i in range(len(dots) - 1):
                start = (l[i][0], l[i + 1][0])
                end = (l[i][1], l[i + 1][1])
                plt.plot(start, end, color='#0085c3')
            plt.show()

        drawPic(l)



if __name__ == '__main__':
    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, "../data/TSPTW_dataset.txt", Encoding.P)
    pop.initialization()
    problem = Classical_TSP(pop_size, chromo_len)
    alg = Algorithm(problem, pop, 100, 0.9, 0.2, 0.2, 0.3)
    alg.draw()

