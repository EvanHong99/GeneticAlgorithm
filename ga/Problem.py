# -*- coding=utf-8 -*-
# @File     : Problem.py
# @Time     : 2022/10/4 17:25
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description: 问题类是用来存储与待求解问题相关信息的一个类。

import os
from typing import overload
import numpy as np


class Problem:
    def __init__(self):
        """
        存放目标函数的参数
        """
        pass

    @overload
    def objective_func(self):
        pass
