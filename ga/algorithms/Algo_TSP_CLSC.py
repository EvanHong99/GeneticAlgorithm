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
        self.best_res=None

    def run(self):
        # prepare
        self.population.initialization()  # read data, construct the herd
        self.problem.init_cost(self.population.info)
        fit = np.array(list(map(self.problem.calc_fitness, self.population.individuals)))
        obj = self.problem.objective_func(all_fitness=fit)
        print("obj init: ", obj)
        elites=None
        bads=None
        best_fit=0
        threshold=3
        counter=0
        old_obj=obj
        for generation in range(self.MAXGEN):
            # reintroduce
            if elites is not None:
                self.population.individuals[bads] = self.population.individuals[elites]

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

            # elite selection
            elites, bads = self.ope_sel.select(fit)
            if fit[elites[0]]>best_fit:
                self.best_res=self.population.individuals[elites[0]]
                best_fit=fit[elites[0]]

            # print score
            fit = np.array(list(map(self.problem.calc_fitness, self.population.individuals)))
            obj = self.problem.objective_func(all_fitness=fit)
            if generation%50==0:
                print(f"obj {generation}: ", obj)

            # update parameters
            if obj<=old_obj: counter+=1
            else: counter=0
            if counter>=threshold:
                self.ope_sel.pos = min(0.05+self.ope_sel.pos,0.7)# going up
                self.ope_cro.poc = max(self.ope_cro.poc-0.02,0.05) # going down
                self.ope_cro.proportion = max(self.ope_cro.proportion-0.05,0.1) # going down
                self.ope_mut.pom = min(self.ope_mut.pom+0.02,0.2) # slowly going up
                counter=0
                print("update operators")


        return obj,best_fit,self.best_res


if __name__ == '__main__':
    pop_size = 100
    chromo_len = 100
    pop = Population(pop_size, chromo_len, "../../data/TSPTW_dataset.txt", Encoding.P)
    problem = Classical_TSP(pop_size, chromo_len)
    alg = Algo_TSP_CLSC(problem, pop, 500, 0.1, 0.1, 0.5, 0.2)

    obj,bestfit,best=alg.run()
    np.savetxt(
        f"../../output/res/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{obj}.txt",
        best, fmt='%i', delimiter=",")

    alg.draw(best,save_path=f"../../output/pics/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{obj}.png")
