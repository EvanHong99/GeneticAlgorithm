# -*- coding=utf-8 -*-
# @File     : Algorithm.py
# @Time     : 2022/10/4 17:23
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description: 算法设置类是用来存储与算法运行参数设置相关信息的一个类。

from Population import Population
from Problem import Problem
from bitarray import bitarray

'''
算法流程
Step1：对解空间进行编码；
Step2：随机产生包含n个个体的初始群体； 
Step3：适应度评估检测个体适应度；
Step4：while< 为满足迭代终止条件>； 
Step5：利用选择算子选择出若干个体进入交配池；
Step6：随机选择交配池中的两个个体，按照交叉概率进行交叉操
作；
Step7：变异算子通过按变异概率随机反转某些（个） 基因位；
Step8：适应度评估检测个体适应度； 
Step9：end
'''

class Algorithm:
    """
    Algorithm : class - 算法类的顶级父类
    描述:
        算法设置类是用来存储与算法运行参数设置相关信息的一个类。
    属性:
        name            : str      - 算法名称（可以自由设置名称）。

        problem         : class <Problem> - 问题类的对象。
        population      : class <Population> - 种群对象。

        MAXGEN          : int      - 最大进化代数。

        currentGen      : int      - 当前进化的代数。

        MAXTIME         : float    - 时间限制（单位：秒）。

        timeSlot        : float    - 时间戳（单位：秒）。

        passTime        : float    - 已用时间（单位：秒）。

        MAXEVALS        : int      - 最大评价次数。

        evalsNum        : int      - 当前评价次数。

        MAXSIZE         : int      - 最优个体的最大数目。
        outFunc         : function - 提供给用户自定义的函数，它在每发生一次进化时被调用。如果没有定义，则默认为None。

        logTras         : int      - Tras即周期的意思，该参数用于设置在进化过程中每多少代记录一次日志信息。
                                     设置为0表示不记录日志信息。
                                     注：此时假如设置了“每10代记录一次日志”而导致最后一代没有被记录，
                                         则会补充记录最后一代的信息，除非找不到可行解。
        log             : Dict     - 日志记录。其中包含2个基本的键：'gen'和'eval'，其他键的定义由该算法类的子类实现。
                                     'gen'的键值为一个list列表，用于存储日志记录中的每一条记录对应第几代种群。
                                     'eval'的键值为一个list列表，用于存储进化算法的评价次数。
                                     注：若设置了logTras为0，则不会记录日志，此时log会被设置为None。

        verbose         : bool     - 表示是否在输入输出流中打印输出日志信息。
        stopMsg         : str      - 记录进化终止原因的字符串。
        dirName         : str      - 用于指明文件保存的路径。用于把绘图文件保存在此目录下。
                                     当缺省或为None时，默认dirName=''，此时如果绘制图片，图片会被保存在执行文件的所在目录下。
    函数:
        __init__()       : 构造函数，定义一些属性，并初始化一些静态参数。
        initialization() : 在进化前对算法类的一些动态参数进行初始化操作，具体功能需要在继承类中实现。

        run()            : 执行函数，具体功能需要在继承类中实现。
        logging()        : 用于在进化过程中记录日志，具体功能需要在继承类中实现。
        stat()           : 用于分析当代种群的信息，具体功能需要在继承类中实现。
        terminated()     : 计算是否需要终止进化，具体功能需要在继承类中实现。
        finishing ()     : 进化完成后调用的函数，具体功能需要在继承类中实现。
        check()          : 用于检查种群对象的ObjV和CV的数据是否有误。
        call_aimFunc()   : 用于调用问题类中的aimFunc()或evalVars()进行计算ObjV和CV(若有约束)。
        display()        : 用于在进化过程中进行一些输出，需要依赖属性verbose和log属性。
"""
    def __init__(self,problem:Problem,population:Population,MAXGEN):
        self.MAXGEN = MAXGEN
        self.population = population
        self.problem=problem

        pass
