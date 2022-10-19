# -*- coding=utf-8 -*-
# @File     : MOEA_TSP_Timewindow.py
# @Time     : 2022/10/19 21:51
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:


import numpy as np
import geatpy as ea
import os
import pandas as pd


class MOEA_TSP_Timewindow(ea.Problem):  # 继承Problem父类
    def __init__(self, testName, fpath):  # testName为测试集名称
        name = testName  # 初始化name
        # 读取城市坐标数据
        self.data = pd.read_csv(fpath, delimiter="\s+", header=0)
        self.places = self.data[["XCOORD", "YCOORD"]].values
        M = 3  # 初始化M（目标维数）
        Dim = self.places.shape[0]  # 初始化Dim（决策变量维数）
        maxormins = [1, -1,1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [0] * Dim  # 决策变量下界
        ub = [Dim - 1] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def evalVars(self, Vars):  # 目标函数
        N = Vars.shape[0]  # N个个体
        # 添加最后回到出发地
        X = np.hstack([Vars, Vars[:, [0]]]).astype(int)
        ObjV = []  # 存储所有种群个体对应的总路程
        # X[i] is an individual
        all_dist = []
        all_profit = []
        all_time_penalty=[]
        for i in range(N):
            # print("X[i]",X[i])
            path=X[i]
            journey = self.places[path, :]  # 按既定顺序到达的地点坐标
            time_window_l=self.data["READY_TIME"]
            time_window_r=self.data["DUE_TIME"]
            distance_intervals=np.sqrt(np.sum(np.diff(journey.T) ** 2, 0))
            time_penalty=0
            current_time=0
            for i in range(len(distance_intervals)):
                current_time+=distance_intervals[i]
                temp=time_window_l[path[i + 1]]-current_time
                if temp>0:
                    time_penalty+=temp
                    continue
                else:
                    temp=current_time-time_window_r[path[i + 1]]
                    if temp>0:
                        time_penalty+=temp
                        continue
            distance = np.sum(distance_intervals)  # 计算总路程
            profit = np.sum(self.data.loc[X[i], "PROFIT"])
            all_dist.append(distance)
            all_profit.append(profit)
            all_time_penalty.append(time_penalty)
            # ObjV.append(distance - self.weight * profit)
        all_dist=np.array([all_dist]).T
        all_profit=np.array([all_profit]).T
        all_time_penalty=np.array([all_time_penalty]).T
        # print(all_dist)
        # print(all_profit)
        f = np.hstack([all_dist, all_profit,all_time_penalty])
        # print(f)
        return f