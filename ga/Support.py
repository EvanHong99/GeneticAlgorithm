# -*- coding=utf-8 -*-
# @File     : Support.py
# @Time     : 2022/10/8 21:03
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description:
from enum import Enum

class ChromeRepr(Enum):
    """
    gene representation
    """
    BIN=0
    REAL=1
    P=2 # Permutation Chromosomes, such as gene in TSP problem