# COMP5511 Artificial Intelligence Concepts - Assignment 1

## Special Features

- Well managed GitHub repository with formal format.

## Problem Restatement

0. Overall target
    - [x] give the details of the designed algorithms
    - [ ] perform sensitive studies for
the above tasks with the various parameters, for example, the crossover and mutation rates,
the population size, and the number of generations, discuss the effects of changing these
parameters
    - [x] show their results in various formats, such as tables, figures,
etc.
    - [ ] Introduction: Give a brief introduction about TSP, GA, etc.
? Methodology: Include five subsection regarding the five tasks. In each
subsection, you should give a detailed description of the designed algorithm,
including the overall framework, crossover and mutation operators, selection
operator, and other components.
? Experimental results: Include five subsection regarding the five tasks. In
each subsection, you should provide the experimental results and carry out
sensitive studies with the various parameters, e.g., the population size, and
discuss the effects of changing these parameters. You need to show the
results in various formats, such as tables, figures, etc.
? Conclusion: You should summarize what you have learned and your
findings.


1. Classical TSP
    - [x] find the shortest round-trip route of these 100 customers
    - [x] visualize the round-trip route
    - [x] calculate total distance


2. Dynamic optimization problem
    - [ ] tackle the problem that customers and positions are changing
    - [ ] reuse/not reuse the solutions from the last environment, and then **compare the results**
    - [ ] visualize the round-trip route
    - [ ] calculate total distance
        需要利用上一个environment的最短路径来加速下一environment。是否可以视为将新的customer一个个插入，我们根据距离和现有的访问顺序来决定插入在哪两个customer中间


3. Large-scale optimization problem
    - [ ] cluster
    先根据chromosome聚类，GA，再合并


4. Multi-objective optimization problem
    - [ ] minimize the travel distance and maximize the sales profit, but perhaps they can't be satisfied at the same time
    - [ ] weighting objective functions-based method $min(distence-\labmda profit)$, Students can specify the ? value to get the optimal solution
    - [ ] students should develop a **Pareto dominance selection-based evolutionary algorithm（基于选择的帕累托改进进化算法）** 
    to handle the multi-objective optimization problem and discuss the advantages 
    and disadvantages of the weighting objective functions-based method 
    and Pareto dominance selection-based method.


**sales profit of each customer can be randomly generated between [1,50]**, the two objective functions, (i.e., total travel distance ? and total sales profit ?%) may
be conflicting, that is, a solution cannot satisfy the maximal sales profit and minimal travel
distance at the same time. 



moea_awGA_templet	多目标优化awGA算法模板

5. Time window constraint problem 需要在规定时间窗口内到访指定客户早到晚到都会受到penalty
    - [ ] travel time between customers is computed by the Euclidean distance between customers
    - [ ] students are required to develop a Pareto dominance selection-based
evolutionary algorithm to solve the problem by optimizing the following three objectives:
minimize total travel distance, maximize total sales profit, and minimize the total violation
value of the time window, where the total violation value of the time window is the
summation of the violation value of the time window for each customer. For example, “READY
TIME” and “DUE TIME” of the “CUST NO 3” are 2 and 61, respectively. If the salesman visits
the “CUST NO 3” at time 63, the violation value of the time window is 63-61=2. If the salesman
visits the “CUST NO 3” at time 1, the violation value of the time window is 2-1=1.
    - [ ] 因此多目标优化大多数场景下无法得到在各个目标上都达到最优的结果。只能达到Pareto最优
    
    高斯变异
在进行变异时用一个均值为μ（μ实际上等于要变异的值）、方差为σ2的正态分布的一个随机数来替换原有基因值。也就是意味着以此数值为期望，以σ2（任取）为方差的正态分布中的一个值替换掉此数值。

高斯变异的局部搜索能力较好，但是引导个体跳出局部较优解的能力较弱，不利于全局收敛

多目标优化
多目标优化研究多于一个的目标函数在给定区域上的最优化，在很多实际问题中，例如经济、管理、军事、科学和工程设计等领域，衡量一个方案的好坏往往难以用一个指标来判断，而需要用多个目标来比较，而这些目标有时不甚协调，甚至是矛盾的。因此多目标优化大多数场景下无法得到在各个目标上都达到最优的结果。只能达到Pareto最优

6. Other Features
    - [x] python `@overload` decorator

## Task 1

- [x] find the shortest round-trip route of these 100 customers
- [x] visualize the round-trip route
- [x] calculate total distance

### Fitness

In Classic TSP, lower distance means better fitness score, 
so I use the inverse of distance to represent fitness.

Coefficient 1000 makes fitness closer to 0, preventing from losing precision. 

$$ fitness= 1000/distance $$

### Selection - Weighted Fitness

Calculate the fitness of each chromosome, and the greater chance to be selected
if the fitness is larger.

Note that in consequence of the transformation function $fitness=1000/distance$,
the transform is nonlinear, so it is easier for my program to converge.

![fitness function](imgs/fitness.png)

### Selection - Elite

Select individuals with the highest fitness, 
reintroduce them by replacing the worst individuals in the next loop.

Higher proportion of elites means our algorithm can reach the local optimum faster,
but lower probability to jump out of local optimum.

### Crossover - Recombination

My algorithm is the same as Professor showed in the class.

I add some features that the probability of crossover and proportion of genes are self-defined,
so it will be easier to converge.

![recombination](imgs/recombination.png)

### Mutation - Swap

Classic TSP not allows repeating points, so swap two genes is a good way to perform mutation.

Also, a parameter `pom(probability of mutation)` is added, in order to control the program.

### Objective Function - To evaluate whole population

I choose mean of fitnesses to represent it.