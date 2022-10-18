# -*- coding=utf-8 -*-
# @File     : Algo_TSP_Cluster.py
# @Time     : 2022/10/15 15:09
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

import numpy as np
from ga.algorithms.__init__ import *


class Algo_TSP_Cluster(Algorithm):
    """
    By adding 100 to the X coordinate for each customer in the TSPTW_dataset.txt, additional
100 customers can be formed.
Regarding the newly formed 100 customers and the original
100 customers as a whole, the new problem can be regarded as a large-scale problem.
For
this large-scale problem, the customers can be divided into several small-scale regions by
using clustering techniques, e.g., K-means. The salesman must finish visiting all the customers
within the region before visiting any other customers in other regions.
In this task, students
are required to combine the clustering technique with a genetic algorithm to handle the large-scale optimization problem.
    """

    def __init__(self, problem, population, MAXGEN, pos, poc, proportion, pom, pocc, pocm, n_clusters=4):
        super(Algo_TSP_Cluster, self).__init__(problem, population, MAXGEN, pos, poc, proportion, pom)
        self.ope_esel = ElitismSelection(pos)
        self.ope_fsel = FitnessSelection()
        self.ope_cro = ClusterRecombination(poc, proportion, pocc)
        self.ope_mut = ClusterSwapMutation(pom, pocm)
        self.best_res = None
        self.n_clusters = n_clusters

    def __str__(self):
        return "Algo_TSP_Cluster"

    def run(self):
        # prepare
        self.population.init_info()  # read data
        self.population.init_shift_info(100)
        clustered_index = self.population.get_cluster(self.n_clusters)
        print("clustered_index", clustered_index)
        self.population.init_individuals(cluster=clustered_index)
        print("individuals.shape", self.population.individuals.shape, self.population.info.shape)
        self.problem.init_cost(self.population.info)

        elites = None
        bads = None
        obj = None
        best_fit = 0
        dist_history = []
        threshold = 5
        counter = 0
        old_obj = 0

        for generation in range(self.MAXGEN):
            # reintroduce
            if elites is not None:
                self.population.individuals[bads] = self.population.individuals[elites]

            # fitness selection
            fit = np.array(list(
                map(self.problem.calc_fitness, self.population.individuals, [Encoding.CP] * self.population.pop_size)))
            selected = self.ope_fsel.select(fit)
            self.population.individuals = self.population.individuals[selected]

            # crossover
            # print('**0**'*10)

            for idx in range(generation, int(self.population.pop_size / 2) + generation):
                parent1 = (2 * idx) % self.population.pop_size
                parent2 = (2 * idx + 1) % self.population.pop_size
                child1, child2 = self.ope_cro.crossover(
                    self.population.individuals[parent1],
                    self.population.individuals[parent2], self.n_clusters)
                self.population.individuals[parent1] = child1
                self.population.individuals[parent2] = child2
            # print('**1**'*10)

            # mutation
            self.population.individuals = np.array(list(
                map(self.ope_mut.mutate, self.population.individuals, [self.n_clusters] * self.population.pop_size)))
            # print('**2**'*10)

            # elite selection
            fit = np.array(list(
                map(self.problem.calc_fitness, self.population.individuals, [Encoding.CP] * self.population.pop_size)))
            obj = self.problem.objective_func(all_fitness=fit)
            elites, bads = self.ope_esel.select(fit)
            if fit[elites[0]] > best_fit:
                self.best_res = self.population.individuals[elites[0]]
                best_fit = fit[elites[0]]

            # print score and preserve history
            if generation % 50 == 0:
                print(f"obj {generation}: ", obj)
                dist_history.append(self.problem.fitness_preimage(fit[elites[0]]))

            # update parameters

            # if obj <= old_obj:
            #     counter += 1
            #     if counter >= threshold:
            #         self.ope_esel.pos = min(0.05 + self.ope_esel.pos, 0.7)  # going up
            #         self.ope_cro.poc = max(self.ope_cro.poc - 0.02, 0.05)  # going down
            #         self.ope_cro.proportion = max(self.ope_cro.proportion - 0.05, 0.1)  # going down
            #         self.ope_mut.pom = min(self.ope_mut.pom + 0.02, 0.2)  # slowly going up
            #         counter = 0
            #         print("update operators")
            # else:
            #     old_obj=obj
            #     counter = 0

        return obj, best_fit, self.best_res, dist_history


if __name__ == '__main__':
    pop_size = 100
    chromo_len = 100
    n_cluster = 4
    root="/content/drive/MyDrive/Github/GeneticAlgorithm"
    pop = Population(pop_size, chromo_len, root+"/data/TSPTW_dataset.txt", Encoding.CP)
    pop.init_info()
    problem = Classical_TSP(1e6)
    alg = Algo_TSP_Cluster(problem, pop, 10000, 0.1, 0.1, 0.5, 0.2, 0.01, 0.01, n_cluster)
    #
    obj, bestfit, best, dist_history = alg.run()
    best = pop.flatten_chromosome(best)
    np.savetxt(
        root+f"/output/res/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{obj}.txt",
        best, fmt='%i', delimiter=",")

    alg.draw(best, save_path=root+f"/output/pics/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{obj}.png")
