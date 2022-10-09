# -*- coding=utf-8 -*-
# @File     : BaseSelection.py
# @Time     : 2022/10/9 10:20
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:

import numpy as np
from typing import overload

class BaseSelection(object):

    def __init__(self):
        pass

    @overload
    def select(self,fitness:np.ndarray):
        pass