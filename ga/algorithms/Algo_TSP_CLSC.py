# -*- coding=utf-8 -*-
# @File     : Algo_TSP_CLSC.py
# @Time     : 2022/10/12 17:01
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:
import numpy as np

from Algorithm import Algorithm
from Population import Population
from problems.Classical_TSP import *
from operators.Crossover.Recombination import Recombination
from operators.Selection.ElitismSelection import ElitismSelection
from operators.Mutation.SwapMutation import SwapMutation
from Support import *
from typing import overload, Union
import datetime


class Algo_TSP_CLSC(Algorithm):
    def __init__(self, problem: Classical_TSP, population: Population, MAXGEN, pos, poc, proportion, pom):
        super(Algo_TSP_CLSC, self).__init__(problem, population, MAXGEN, pos, poc, proportion, pom)
        self.ope_sel = ElitismSelection(pos)
        self.ope_cro = Recombination(poc, proportion)
        self.ope_mut = SwapMutation(pom)

    def run(self):
        # prepare
        self.population.initialization()  # read data, construct the herd
        self.problem.init_cost(self.population.info)
        fit = np.array(list(map(self.problem.calc_fitness, self.population.individuals)))
        obj = self.problem.objective_func(all_fitness=fit)
        print("obj init: ", obj)
        # elites=None
        # bads=None
        #
        for generation in range(self.MAXGEN):
            # todo reintroduce
            # if elites is not None:
            #     pass

            # selection
            elites, bads = self.ope_sel.select(fit)
            self.history.append(self.population.individuals[elites][0])
            if generation == 0:
                print("elites ",self.population.individuals[elites][0])
            # if generation == 0:
            #     print("before reintroduce ", self.population.individuals[bads][0])
            self.population.individuals[bads] = self.population.individuals[elites]
            # if generation == 0:
            #     print("after reintroduce ", self.population.individuals[bads][0])

            # crossover
            for idx in range(generation, int(self.population.pop_size / 2) + generation):
                parent1=(2 * idx) % self.population.pop_size
                parent2=(2 * idx) % self.population.pop_size+1
                child1, child2 = self.ope_cro.crossover(
                    self.population.individuals[parent1],
                    self.population.individuals[parent2])
                self.population.individuals[parent1]=child1
                self.population.individuals[parent2]=child2

            # mutation
            self.population.individuals=np.array(list(map(self.ope_mut.mutate,self.population.individuals)))
            if generation == 0:
                print("after mutation ", self.population.individuals[0])

            # print score
            fit = np.array(list(map(self.problem.calc_fitness, self.population.individuals)))
            obj = self.problem.objective_func(all_fitness=fit)
            print(f"obj {generation}: ", obj)

        elites, bads = self.ope_sel.select(fit)
        return obj,self.population.individuals[elites]


if __name__ == '__main__':
    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, "../../data/TSPTW_dataset.txt", Encoding.P)
    problem = Classical_TSP(pop_size, chromo_len)
    alg = Algo_TSP_CLSC(problem, pop, 500, 0.9, 0.2, 0.2, 0.3)

    obj,elites=alg.run()
    print(elites)
    with open('../../output/res.txt','a') as fw:
        fw.writelines(f"{'*' * 20}= {datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')} ={'*' * 20}\n")
        fw.write(f"{obj}\n")
        fw.writelines(str(elites))
        fw.writelines('\n' * 3)

    alg.draw(alg.history[-1])
