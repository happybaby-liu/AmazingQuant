# -*- coding: utf-8 -*-

# ------------------------------
# @Time    : 2020/3/31
# @Author  : gao
# @File    : ic_analysis.py
# @Project : AmazingQuant
# ------------------------------
"""
IC分析
IC是指因子在第T期的因子值与T+1期的股票收益的相关系数
1.计算rank_IC
2.评价指标
    （1） IC均值
    （2） IC标准差
    （3） IC_IR比率
    （4） IC>0占比
    （5） |IC|>0.02占比(绝对值)
    （6） p-value（有效性）,全部都计算时间序列
    （7） IC信号衰减计算
"""