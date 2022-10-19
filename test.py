# -*- coding=utf-8 -*-
# @File     : test.py
# @Time     : 2022/10/8 20:55
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:
import time
import numpy as np
import pandas as pd
import datetime
from Population import Population
from ga.problems.Classical_TSP import Classical_TSP


def shuffle(cluster: list[list]):
    for i in range(len(cluster)):
        np.random.shuffle(cluster[i])
    np.random.shuffle(cluster)

def map_cluster(chromo1,chromo2):
    mapper=[]
    table=np.zeros(len(chromo1))
    for i in range(len(chromo1)):
        gene1=set(chromo1[i])
        for j in range(len(chromo2)):
            if table[j]==1:
                continue
            if set(chromo2[j])==gene1:
                table[j]=1
                mapper[i]=j
    return mapper


def gen_profit():
    data=pd.read_csv('data/TSPTW_dataset.txt', sep='\s+', header=0)
    data['PROFIT']=np.random.rand(data.shape[0])*49+1
    print(data)
    data.to_csv("data//TSPTW_dataset_profit.txt", sep='\t',index=['CUST_NO'])
    data1=pd.read_csv('data/TSPTW_dataset_profit.txt', sep='\s+', header=0)
    print(data1)


if __name__ == '__main__':

    # cluster=[[0,1,2,3],[4,5],[6,7,8]]
    # cluster1=[[0,1],[2,3,4,5],[6,7,8,9,10]]
    # individuals=[]
    # shuffle(cluster)
    # # print(cluster)
    # shuffle(cluster1)
    # individuals.append(cluster)
    # individuals.append(cluster1)
    # # print(individuals)
    # individuals=np.array(individuals,dtype=object)
    # # print(individuals)
    # # print(Population.flatten_chromosome(individuals[0]))
    # #
    # # prob=Classical_TSP(100,100)
    # # cost=np.random.rand(100,100)
    # # prob.cost=cost
    # # print(prob.cost)
    # # routine=np.arange(100)
    # # np.random.shuffle(routine)
    # # print(routine)
    a=pd.Series(data=[1,2,3,4])
    print(np.sum(a))
