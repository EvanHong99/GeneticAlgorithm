# -*- coding=utf-8 -*-
# @File     : Algo_TSP_Dynamic.py
# @Time     : 2022/10/13 22:08
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

from ga.Algorithm import Algorithm
import numpy as np
from Algorithm import Algorithm
from Population import Population
from problems.Classical_TSP import *
from operators.Crossover.Recombination import Recombination
from operators.Selection.ElitismSelection import ElitismSelection
from operators.Selection.FitnessSelection import FitnessSelection
from operators.Mutation.SwapMutation import SwapMutation
from Support import *
from typing import overload, Union
import datetime


class Algo_TSP_Dynamic(Algorithm):
    def __init__(self, problem:Classical_TSP , population: Population, MAXGEN, pos, poc, proportion, pom):
        super(Algo_TSP_Dynamic, self).__init__(problem, population, MAXGEN, pos, poc, proportion, pom)
        self.ope_esel = ElitismSelection(pos)
        self.ope_fsel=FitnessSelection()
        self.ope_cro = Recombination(poc, proportion)
        self.ope_mut = SwapMutation(pom)
        self.best_res = None

    def run(self):
        # prepare
        self.population.initialization()  # read data, construct the herd
        self.problem.init_cost(self.population.info)
        elites = None
        bads = None
        obj=None
        best_fit = 0
        threshold = 10
        counter = 0
        old_obj = 0
        env=0
        for generation in range(self.MAXGEN):
            if generation%100==0 and env<=5 :
                if env!=0:
                    self.population.add_individuals(10)
                    self.population.update_info(env)
                    self.problem.init_cost(self.population.info)
                env += 1
            # reintroduce
            if elites is not None:
                self.population.individuals[bads] = self.population.individuals[elites]


            # fitness selection
            fit = np.array(list(map(self.problem.calc_fitness, self.population.individuals)))
            selected=self.ope_fsel.select(fit)
            self.population.individuals=self.population.individuals[selected]

            # crossover
            for idx in range(generation, int(self.population.pop_size / 2) + generation):
                parent1 = (2 * idx) % self.population.pop_size
                parent2 = (2 * idx) % self.population.pop_size + 1
                child1, child2 = self.ope_cro.crossover(
                    self.population.individuals[parent1],
                    self.population.individuals[parent2])
                self.population.individuals[parent1] = child1
                self.population.individuals[parent2] = child2

            # mutation
            self.population.individuals = np.array(list(map(self.ope_mut.mutate, self.population.individuals)))

            # print score
            fit = np.array(list(map(self.problem.calc_fitness, self.population.individuals)))
            obj = self.problem.objective_func(all_fitness=fit)
            if generation % 50 == 0:
                print(f"obj {generation}: ", obj)

            # elite selection
            elites, bads = self.ope_esel.select(fit)
            if fit[elites[0]] > best_fit and env==6:
                self.best_res = self.population.individuals[elites[0]]
                best_fit = fit[elites[0]]

            # update parameters
            if obj <= old_obj:
                counter += 1
                if counter >= threshold:
                    self.ope_esel.pos = min(0.05 + self.ope_esel.pos, 0.7)  # going up
                    self.ope_cro.poc = max(self.ope_cro.poc - 0.02, 0.05)  # going down
                    self.ope_cro.proportion = max(self.ope_cro.proportion - 0.05, 0.1)  # going down
                    self.ope_mut.pom = min(self.ope_mut.pom + 0.02, 0.2)  # slowly going up
                    counter = 0
                    print("update operators")
            else:
                old_obj=obj
                counter = 0


        return obj, best_fit, self.best_res


if __name__ == '__main__':
    pop_size = 50
    chromo_len = 50
    pop = Population(pop_size, chromo_len, "../../data/TSPTW_dataset.txt", Encoding.P)
    problem = Classical_TSP(100, 100)
    alg = Algo_TSP_Dynamic(problem, pop, 700, 0.1, 0.1, 0.5, 0.2)

    obj, bestfit, best = alg.run()
    np.savetxt(
        f"../../output/res/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{obj}.txt",
        best, fmt='%i', delimiter=",")

    alg.draw(best, save_path=f"../../output/pics/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{obj}.png")
