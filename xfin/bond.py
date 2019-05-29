#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   bond.py
@Version :   1.0.0
@Author  :   xiaxianba
@License :   (C) Copyright 2006-2019
@Contact :   xiaxianba@qq.com
@Software:   PyCharm
@Time    :   2019/5/29 9:33
@Desc    :
"""


def cur_bond_value(par, coupon_rate, maturity, base_rate):
    """
    Func: Calculating the current value of bonds
    @Param:
    """
    bond_value = 0.0

    year = int(maturity)
    fraction = maturity - year
    for n in range(1, year+1):
        bond_value += (par*coupon_rate)/(1+base_rate)**n
        if n == year:
            bond_value += par/(1+base_rate)**n
    # print bond_value
    if fraction > 0:
        bond_value = bond_value/(1+base_rate)**fraction
    # print bond_value
    return bond_value


# @TEST
cur_bond_value(100, 0.08, 2.5, 0.06)

