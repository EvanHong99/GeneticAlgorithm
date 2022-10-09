# COMP5511 Artificial Intelligence Concepts - Assignment 1

## Problem Restatement
0. Overall target
    - [ ] give the details of the designed algorithms
    - [ ] perform sensitive studies for
the above tasks with the various parameters, for example, the crossover and mutation rates,
the population size, and the number of generations
    - [ ] discuss the effects of changing these
parameters
    - [ ] show their results in various formats, such as tables, figures,
etc.

1. Classical TSP
    - [ ] find the shortest round-trip route of these 100 customers
    - [ ] visualize the round-trip route
    - [ ] calculate total distance

2. Dynamic optimization problem
    - [ ] tackle the problem that customers and positions are changing
    - [ ] reuse/not reuse the solutions from the last environment, and then **compare the results**
    - [ ] visualize the round-trip route
    - [ ] calculate total distance
        ��Ҫ������һ��environment�����·����������һenvironment���Ƿ������Ϊ���µ�customerһ�������룬���Ǹ��ݾ�������еķ���˳��������������������customer�м�


3. Large-scale optimization problem
    - [ ] cluster
    �ȸ���chromosome���࣬GA���ٺϲ�

4. Multi-objective optimization problem
    - [ ] minimize the travel distance and maximize the sales profit, but perhaps they can't be satisfied at the same time
    - [ ] weighting objective functions-based method $min(distence-\labmda profit)$, Students can specify the ? value to get the optimal solution
    - [ ] students should develop a **Pareto dominance selection-based evolutionary algorithm������ѡ��������иĽ������㷨��** 
    to handle the multi-objective optimization problem and discuss the advantages 
    and disadvantages of the weighting objective functions-based method 
    and Pareto dominance selection-based method.

**sales profit of each customer can be randomly generated between [1,50]**, the two objective functions, (i.e., total travel distance ? and total sales profit ?%) may
be conflicting, that is, a solution cannot satisfy the maximal sales profit and minimal travel
distance at the same time. 



moea_awGA_templet	��Ŀ���Ż�awGA�㷨ģ��

5. Time window constraint problem ��Ҫ�ڹ涨ʱ�䴰���ڵ���ָ���ͻ��絽�������ܵ�penalty
    - [ ] travel time between customers is computed by the Euclidean distance between customers
    - [ ] students are required to develop a Pareto dominance selection-based
evolutionary algorithm to solve the problem by optimizing the following three objectives:
minimize total travel distance, maximize total sales profit, and minimize the total violation
value of the time window, where the total violation value of the time window is the
summation of the violation value of the time window for each customer. For example, ��READY
TIME�� and ��DUE TIME�� of the ��CUST NO 3�� are 2 and 61, respectively. If the salesman visits
the ��CUST NO 3�� at time 63, the violation value of the time window is 63-61=2. If the salesman
visits the ��CUST NO 3�� at time 1, the violation value of the time window is 2-1=1.
    - [ ] ��˶�Ŀ���Ż�������������޷��õ��ڸ���Ŀ���϶��ﵽ���ŵĽ����ֻ�ܴﵽPareto����
    
    ��˹����
�ڽ��б���ʱ��һ����ֵΪ�̣���ʵ���ϵ���Ҫ�����ֵ��������Ϊ��2����̬�ֲ���һ����������滻ԭ�л���ֵ��Ҳ������ζ���Դ���ֵΪ�������Ԧ�2����ȡ��Ϊ�������̬�ֲ��е�һ��ֵ�滻������ֵ��

��˹����ľֲ����������Ϻã������������������ֲ����Ž������������������ȫ������

��Ŀ���Ż�
��Ŀ���Ż��о�����һ����Ŀ�꺯���ڸ��������ϵ����Ż����ںܶ�ʵ�������У����羭�á��������¡���ѧ�͹�����Ƶ����򣬺���һ�������ĺû�����������һ��ָ�����жϣ�����Ҫ�ö��Ŀ�����Ƚϣ�����ЩĿ����ʱ����Э����������ì�ܵġ���˶�Ŀ���Ż�������������޷��õ��ڸ���Ŀ���϶��ﵽ���ŵĽ����ֻ�ܴﵽPareto����

6. Other Features
    - [x] python `@overload` decorator

## Task 1