# -*- coding=utf-8 -*-
# @File     : BaseMutation.py
# @Time     : 2022/10/8 19:36
# @Author   : EvanHong
# @Email    : 939778128@qq.com
# @Project  : code
# @Description: mutation基类

from typing import overload


class BaseMutation:
    def __init__(self):
        pass

    @overload
    def mutate(self):
        pass
