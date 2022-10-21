# -*- coding=utf-8 -*-
# @File     : run_geatpy.py
# @Time     : 2022/10/15 10:43
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:
import json

import numpy as np
from ga.Algorithm import Algorithm
from ga.algorithms.Algo_TSP_CLSC import Algo_TSP_CLSC
from ga.Population import Population
from ga.problems.Classical_TSP import Classical_TSP
from ga.operators.Crossover.Recombination import Recombination
from ga.operators.Selection.ElitismSelection import ElitismSelection
from ga.operators.Mutation.SwapMutation import SwapMutation
from ga.Support import *
from typing import overload, Union
import datetime
import geatpy as ea
from  ga.problems.SOEA_TSP import SOEA_TSP
from  ga.problems.MOEA_TSP import MOEA_TSP
from  ga.problems.MOEA_TSP_Timewindow import MOEA_TSP_Timewindow

class Info(object):
    pos = [0.1, 0.15]
    poc = [0.1, 0.15]
    proportion = [0.4, 0.5]
    pom = [0.1, 0.15, 0.2]


def run(algorithm):
    root = "/content/drive/MyDrive/Github/GeneticAlgorithm"

    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, root + "/data/TSPTW_dataset.txt", Encoding.P)
    problem = Classical_TSP(100, 100)
    pos_list = [0.05, 0.1, 0.15]
    poc_list = [0.05, 0.1, 0.15]
    proportion_list = [0.4, 0.5]
    pom_list = [0.1, 0.15, 0.2]
    n = 5
    history = {}
    for pos in pos_list:
        for poc in poc_list:
            for proportion in proportion_list:
                for pom in pom_list:
                    total_distance = 0
                    temp=[]
                    for i in range(n):
                        alg = algorithm(problem, pop, 20000, pos, poc, proportion, pom)

                        obj, bestfit, best, dist_history = alg.run()
                        temp.append(dist_history)
                        distance = alg.problem.fitness_preimage(bestfit)
                        total_distance += distance
                        np.savetxt(
                            root + f"/output/res/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{algorithm}_{pos}_{poc}_{proportion}_{pom}_{distance}.txt",
                            best, fmt='%i', delimiter=" ")

                        alg.draw(best,
                                 save_path=root + f"/output/pics/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{algorithm}_{pos}_{poc}_{proportion}_{pom}_{distance}.png")

                    avg_dist = total_distance / n
                    history[(pos,poc,proportion,pom)]=(avg_dist,temp)
    with open(root+f"/output/history/history.json",'w') as fw:
        json.dump(history,fw)

def run_SOEA_TSP():
    root=""
    saveDir="./geaty_output/SOEA_TSP/"
    problem = SOEA_TSP("SOEA_TSP",root+"./data/TSPTW_dataset_profit.txt",0.5)
    # 构建算法
    algorithm = ea.soea_SEGA_templet(
        problem,
        ea.Population(Encoding='P', NIND=100),
        MAXGEN=1000,  # 最大进化代数
        logTras=0)  # 表示每隔多少代记录一次日志信息，0表示不记录。
    algorithm.mutOper.Pm = 0.2  # 修改变异算子的变异概率
    algorithm.recOper.XOVR = 0.9  # 修改交叉算子的交叉概率
    # 求解
    res = ea.optimize(algorithm,
                      verbose=False,
                      drawing=1,
                      outputMsg=True,
                      drawLog=True,
                      saveFlag=True,
                      dirName=saveDir)
    # print(res)
    print('The best objective value is: %s' % res['optPop'].ObjV[0][0])
    print('The best variables are: ')
    path=[]
    for i in range(res['optPop'].Phen.shape[1]):
        path.append(res['optPop'].Phen[0, i])
    problem.getReferObjV()

    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, "./data/TSPTW_dataset.txt", Encoding.P)
    pop.init_info()
    problem = Classical_TSP(1e6)
    alg = Algo_TSP_CLSC(problem, pop, 100, 0.1, 0.1, 0.5, 0.2)

    alg.draw(path,
             save_path=saveDir+f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{res['optPop'].ObjV[0][0]}.png")

    return res

def run_MOEA_TSP():
    root=""
    saveDir="./geaty_output/MOEA_TSP/"
    problem = MOEA_TSP("MOEA_TSP",root+"./data/TSPTW_dataset_profit.txt")
    # 构建算法
    algorithm = ea.moea_NSGA2_templet(
        problem,
        ea.Population(Encoding='P', NIND=100),
        MAXGEN=100,  # 最大进化代数
        logTras=0)  # 表示每隔多少代记录一次日志信息，0表示不记录。
    algorithm.mutOper.Pm = 0.2  # 修改变异算子的变异概率
    algorithm.recOper.XOVR = 0.9  # 修改交叉算子的交叉概率
    # 求解
    res = ea.optimize(algorithm,
                      verbose=False,
                      drawing=1,
                      outputMsg=True,
                      drawLog=True,
                      saveFlag=True,
                      dirName=saveDir)
    # print(res)
    print('The best objective value is: %s' % res['optPop'].ObjV[0][0])
    print('The best variables are: ')
    path=[]
    for i in range(res['optPop'].Phen.shape[1]):
        path.append(res['optPop'].Phen[0, i])
    problem.getReferObjV()

    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, "./data/TSPTW_dataset.txt", Encoding.P)
    pop.init_info()
    problem = Classical_TSP(1e6)
    alg = Algo_TSP_CLSC(problem, pop, 100, 0.1, 0.1, 0.5, 0.2)

    alg.draw(path,
             save_path=saveDir+f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{res['optPop'].ObjV[0][0]}.png")
    return res

def run_MOEA_TSP_Timewindow():
    root=""
    saveDir="./geaty_output/MOEA_TSP_Timewindow/"
    problem = MOEA_TSP_Timewindow("MOEA_TSP_Timewindow",root+"./data/TSPTW_dataset_profit.txt")
    # 构建算法
    algorithm = ea.moea_NSGA2_templet(
        problem,
        ea.Population(Encoding='P', NIND=100),
        MAXGEN=1000,  # 最大进化代数
        logTras=0)  # 表示每隔多少代记录一次日志信息，0表示不记录。
    algorithm.mutOper.Pm = 0.2  # 修改变异算子的变异概率
    algorithm.recOper.XOVR = 0.9  # 修改交叉算子的交叉概率
    # 求解
    res = ea.optimize(algorithm,
                      verbose=False,
                      drawing=1,
                      outputMsg=True,
                      drawLog=True,
                      saveFlag=True,
                      dirName=saveDir)
    # print(res)
    print('The best objective value is: %s' % res['optPop'].ObjV[0][0])
    print('The best variables are: ')
    path=[]
    for i in range(res['optPop'].Phen.shape[1]):
        path.append(res['optPop'].Phen[0, i])

    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, "./data/TSPTW_dataset.txt", Encoding.P)
    pop.init_info()
    problem = Classical_TSP(1e6)
    alg = Algo_TSP_CLSC(problem, pop, 100, 0.1, 0.1, 0.5, 0.2)

    alg.draw(path,
             save_path=saveDir+f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{res['optPop'].ObjV[0][0]}.png")
    return res

if __name__ == '__main__':
    # run_SOEA_TSP()
    run_MOEA_TSP()
    # run_MOEA_TSP_Timewindow()