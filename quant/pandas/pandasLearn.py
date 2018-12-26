# -*- coding: utf-8 -*-# 

# -------------------------------------------------------------------------------
# Name:         pandasLearn
# Description:  pandas各种方法的使用
# Author:       fushp
# Date:         2018/12/25
# -------------------------------------------------------------------------------

import sys
import pandas as pd

# -------------------------------------------------------------------------------
#
# Description: 重采样(resample)
# 就是转换数据周期
#
# -------------------------------------------------------------------------------

# 当列太多时不换行
pd.set_option('expand_frame_repr', False)

df = pd.read_csv('/Users/fushp/Desktop/finder/work/git/ReviewKnowleagePython/quant/pandas/data/data.csv',
                 #表示从改列名设置为index
                 # index_col=['candle_begin_time'],
                 # 该参数代表跳过第一行
                 skiprows=1,
                 #将指定列的数据识别为日期格式
                 parse_dates=['candle_begin_time']
                 )

print(df)
# 转变为5分钟数据
rule_type = '5T'
period_df = df.resample(rule=rule_type, on='candle_begin_time', base=0, label='left', closed='left').agg(
    {'open': 'first',
     'high': 'max',
     'low': 'min',
     'close': 'last',
     'volume': 'sum',
     })

# 计算这两分钟的数据 平均值 最大值 最小值  等等

print(period_df)
exit()

