# -*- coding=utf-8 -*-
# @File     : run.py
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

